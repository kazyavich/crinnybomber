import inspect
import logging
import os
import re
import subprocess
import sys
import traceback
import webbrowser

import aiohttp.client_exceptions
import click
import phonenumbers
import pkg_resources
import sentry_sdk
from aiohttp import web
from multidict import MultiDict
from sentry_sdk.integrations.aiohttp import AioHttpIntegration

API_REQUIRED_PARAMS = ["number_of_cycles", "phone_code", "phone"]

os.chdir(os.path.join(pkg_resources.get_distribution("b0mb3r").location, "b0mb3r"))

app = web.Application()
routes = web.RouteTableDef()


def retrieve_installed_version():
    package_info = subprocess.run(
        [sys.executable, "-m", "pip", "show", "b0mb3r"], stdout=subprocess.PIPE
    )
    return re.search(br"Version: ([0-9]\.[0-9.]*)", package_info.stdout).group(1)


logging.disable(logging.WARNING)
sentry_sdk.init(
    "https://f9be285af3ff4f949baba007ddebee24@sentry.io/3144601",
    integrations=[AioHttpIntegration()],
    release=retrieve_installed_version().decode(),
)


@click.command()
@click.option("--ip", default="127.0.0.1")
@click.option("--port", default="8080")
@click.option("--skip-updates", is_flag=True, default=False)
@click.option("--repair", "--force-update", is_flag=True, default=False)
def main(ip: str, port: int, skip_updates: bool, repair: bool):
    if repair:
        update(force=True)
    elif not skip_updates:
        update()

    app.add_routes(routes)
    app.add_routes([web.static("/static", "static")])
    open_url(f"http://{ip}:{port}/")
    web.run_app(app, host=ip, port=port)


def update(force: bool = False):
    if force:
        subprocess.run([sys.executable, "-m", "pip", "install", "b0mb3r", "--force-reinstall"],)


def open_url(url: str):
    try:
        if "com.termux" in os.environ.get("PREFIX", ""):  # If device is running Termux
            subprocess.run(
                ["am", "start", "--user", "0", "-a", "android.intent.action.VIEW", "-d", url,],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
    except FileNotFoundError:
        pass
    webbrowser.open(url, new=2, autoraise=True)


def load_services():
    services = os.listdir("services")
    sys.path.insert(0, "services")
    service_classes = {}

    for service in services:
        if service.endswith(".py") and service != "service.py":
            module = __import__(service[:-3])
            for member in inspect.getmembers(module, inspect.isclass):
                if member[1].__module__ == module.__name__:
                    service_classes[module] = member[0]

    return service_classes


async def attack(number_of_cycles: int, phone_code: str, phone: str):
    for _ in range(number_of_cycles):
        for module, service in load_services().items():
            try:
                supported_phone_codes = getattr(module, service).phone_codes
                if len(supported_phone_codes) == 0 or phone_code in supported_phone_codes:
                    await getattr(module, service)(phone, phone_code).run()
            except ValueError as error:
                sentry_sdk.capture_exception(error)
                continue
            except aiohttp.ClientError:
                continue


@routes.get("/")
async def index(_):
    with open("templates/index.html", encoding="utf-8") as template:
        services_count = str(len(load_services()))
        response = template.read().replace("services_count", services_count)
        return web.Response(text=response, content_type="text/html")


@routes.post("/attack/start")
async def start_attack(request):
    try:
        data = await request.post()
        if len(data.items()) == 0:
            data = await request.json()

        for required_param in API_REQUIRED_PARAMS:
            if required_param not in data:
                return web.json_response(
                    {
                        "success": False,
                        "error_code": 400,
                        "error_description": f"You need to specify {required_param}.",
                    },
                    status=400,
                    headers=MultiDict({"Access-Control-Allow-Origin": "*"}),
                )
        phone = re.sub("[^0-9]", "", data["phone"])

        number_of_cycles = int(data["number_of_cycles"])
        if int(number_of_cycles) < 1:
            return web.json_response(
                {
                    "success": False,
                    "error_code": 400,
                    "error_description": "The minimum value for number_of_cycles is 1.",
                },
                status=400,
                headers=MultiDict({"Access-Control-Allow-Origin": "*"}),
            )

        phone_code = data["phone_code"]
        if phone_code == "":
            phone_code = str(phonenumbers.parse("+" + phone).country_code)

        await attack(number_of_cycles, phone_code, phone)

        return web.json_response(
            {"success": True}, headers=MultiDict({"Access-Control-Allow-Origin": "*"})
        )
    except Exception as error:
        sentry_sdk.capture_exception(error)
        formatted_error = f"{type(error).__name__}: {error}"
        return web.json_response(
            {
                "success": False,
                "error_code": 500,
                "error_description": formatted_error,
                "traceback": traceback.format_exc(),
            },
            status=500,
            headers=MultiDict({"Access-Control-Allow-Origin": "*"}),
        )


if __name__ == "__main__":
    main()
