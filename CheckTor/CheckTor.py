import requests

class CheckTor:
    """
        This module checks, Python script can use tor network or not.
        Example:
            *******
            import CheckTor
            ct = CheckTor.CheckTor() # for Tor's default settings
            ct = CheckTor(
                address_of_tor_proxy = "Tor proxy address",
                tor_port = ....
                )
            if ct.check():
                print("Everythink is fine. We are in the Tor")
            else:
                print("We are not in the Tor")
    """


    def __init__(self, tor_port=9050):
        self.proxies = {
            'http': ':'.join(['socks5://127.0.0.1',str(tor_port)]),
            'https': ':'.join(['socks5://127.0.0.1',str(tor_port)]),
        }

    def check(self):
        try:
            ip_address_with_proxy = requests.get(
                "http://httpbin.org/ip",
                proxies=self.proxies
            )
        except requests.exceptions.ProxyError:
            print("Failed to establish a new connection to proxy server. \
Did you forget to run \"systemctl start tor\"")
            return False

        ip_address_without_proxy = requests.get(
            "http://httpbin.org/ip"
        )
        print(ip_address_with_proxy.text)
        print(ip_address_without_proxy.text)

        if ip_address_with_proxy == ip_address_without_proxy:
            return False
        else:
            return True
