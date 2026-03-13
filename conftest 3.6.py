import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption(
        '--language',
        action='store',
        default=None,
        help="Choose language: es, fr, ru, etc."
    )
    parser.addoption(
        '--noproxy',
        action='store_true',
        default=False,
        help="Disable proxy"
    )

@pytest.fixture(scope="function")
def browser(request):
    # Получаем язык из командной строки
    user_language = request.config.getoption("language")
    no_proxy = request.config.getoption("noproxy")
    
    # Настройка Chrome с нужным языком
    options = Options()
    options.add_experimental_option(
        'prefs', {'intl.accept_languages': user_language}
    )
    
    # Прокси (подключается, если не указан --noproxy)
    if not no_proxy:
        # СПИСОК РАБОЧИХ ПРОКСИ (пробуй разные)
        proxies = [
            ("185.162.230.230", "8080"),   # Россия
            ("138.124.53.25", "7443"),      # Германия
            ("194.213.18.200", "443"),      # США
            ("51.79.135.131", "8080"),      # Сингапур
            ("149.88.94.216", "7890"),      # Гонконг
        ]
        
        # Берём первый прокси из списка (можно менять индекс)
        proxy_ip, proxy_port = proxies[0]
        print(f"\n🔌 Использую прокси: {proxy_ip}:{proxy_port}")
        options.add_argument(f'--proxy-server={proxy_ip}:{proxy_port}')
    else:
        print("\n🌐 Работаю без прокси")
    
    # Создаём браузер
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()