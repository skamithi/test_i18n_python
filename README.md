* ``.pot`` file generated using ``xgettext``. Example
```
mkdir po
xgettext --language=Python --keyword=_ --output=po/test_i18n.pot `find *.py`
```
* modified CHARSET in ``.pot`` file to say ``utf-8``
* copy ``.pot`` file to ``en.po``. made changes there. Used ``po-edit``
   * ``apt-get install po-edit``
* run ``setup.py build``
* run ``./test_i18n.py`` to see it print out the correct translation in the
* english po file

*If you add a new translation , run setup.py build_i18n -m to update the 'po'
files.
```
# python setup.py build_i18n -m
running build_i18n
intltool-update -r -g myapp
en: ... done.


 * Current translation support in myapp

en: 20 translated messages, 2 untranslated messages.
msgfmt po/en.po -o build/mo/en/LC_MESSAGES/myapp.mo

```
