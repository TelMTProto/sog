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
TLS_DOMAIN = "www.Yadesh.ir"

# Tag for advertising, obtainable from @MTProxybot
AD_TAG = "8bd7c59cd625d7991b86a77dfbc5fcff"

