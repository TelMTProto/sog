PORT = 443

# name -> secret (32 hex chars)
USERS = {
    "tg":  "00000000000000000000000000000000"
}

MODES = {
    # Classic mode, easy to detect
    "classic": False,

    # Makes the proxy harder to detect
    # Can be incompatible with very old clients
    "secure": False,

    # Makes the proxy even more hard to detect
    # Can be incompatible with old clients
    "tls": True,
}

# The domain for TLS mode, bad clients are proxied there
# Use random existing domain, proxy checks it on start
TLS_DOMAIN = "www.irancell.io"

# Tag for advertising, obtainable from @MTProxybot
AD_TAG = "c9f96504e1e6ffe934f134baf7ca5255"

#7gAAAAAAAAAAAAAAAAAAAAB3d3cuaXJhbmNlbGwuaW8
#curl -o MTProo.sh -L https://git.io/fjo3u && bash MTProo.sh --port 443 --secret 00000000000000000000000000000000 --tag 8bd7c59cd625d7991b86a77dfbc5fcff --tls www.HideProxi.io --disable-updater
