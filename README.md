passkeyring
===========
A python-keyring backend for the 'pass' password manager.

How to install?
---------------
```
python setup.py install
```


How to set passkeyring as the default keyring backend?
------------------------------------------------------

First find the platform-specific directory location to place the configuration file:

```
config_root=$(python -c "import keyring.util.platform_; print(keyring.util.platform_.config_root())")

echo "[backend]
default-keyring=passkeyring.PassKeyring" > $config_root/keyringrc.cfg
```

How to set passkeyring as the keyring to use at runtime?
--------------------------------------------------------
```
import keyring
from passkeyring import PassKeyring

keyring.set_keyring(PassKeyring())
```

And the rest is the same as usual.
