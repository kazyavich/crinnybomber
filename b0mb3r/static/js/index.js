let input = document.querySelector('#phone');
    let intlTelInput;

    document.addEventListener('DOMContentLoaded', function () {
        intlTelInput = window.intlTelInput(input, {
            onlyCountries: ['ru', 'ua', 'kz', 'by'],
            initialCountry: 'ru',
            separateDialCode: true
        });
    });

    document.querySelector("#main-form").addEventListener("submit", async function (e) {
        e.preventDefault();

        document.querySelector('main').style.cssText = "animation: blur; animation-duration: 0.6s; animation-fill-mode: both";
        document.querySelector('footer').style.cssText = "animation: blur; animation-duration: 0.6s; animation-fill-mode: both";
        setTimeout(function () {
            document.querySelector('#block-ui').style.display = "block";
        }, 600);

        let formData = new FormData(document.querySelector('#main-form'));
        formData.append('phone_code', intlTelInput.getSelectedCountryData().dialCode);

        let response = await fetch("/attack/start", {
            method: 'POST',
            body: formData,
        });

        if (!response.ok) {
            console.log(await response.text());
        }

        setTimeout(function () {
            document.querySelector('#block-ui').style.display = "none";
        }, 600);

        document.querySelector('main').style.cssText = "animation: blur; animation-duration: 0.6s; animation-fill-mode: both; animation-direction: reverse";
        document.querySelector('footer').style.cssText = "animation: blur; animation-duration: 0.6s; animation-fill-mode: both; animation-direction: reverse";
    });