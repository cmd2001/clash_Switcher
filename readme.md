# clash Switcher

A simple tools to optimize clash subscribe link.

### Settings

Change your settings in `app.py`, such as `url` and `name_Proxy`.

Modify `rule0, rule1, rule2, rule3` if you want to add custom proxy rules.

### Deployment

Use Apache2 on Debian 10 as example.

First, install apache2, python3, apache2-uwsgi.

```bash
sudo apt install apache2 python3 python3-pip libapache2-mod-uwsgi-py3
```

Then, install python3 extensions.

```bash
sudo pip3 install flask requests uwsgi
```

Move `app.py`, `app.wsgi` to `/var/www/clashSwitcher`, move `app.conf` to `/etc/apache2/sites-available`, create a symbol link in `sites-enabled` by `sudo ln -s /etc/apache2/sites-available/app.conf /etc/apache2/sites-enabled/app.conf`.

Restart apache2 and enjoy it.

### Licenses

GPL v3.