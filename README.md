* ``.pot`` file generated using ``pygettext``
* modified CHARSET in ``.pot`` file to say ``utf-8``
* copy ``.pot`` file to ``en.po``. made changes there. Used ``po-edit``
   * ``apt-get install po-edit``
* run ``setup.py build``
* run ``./test_i18n.py' to see it print out the correct translation in the
* english po file

