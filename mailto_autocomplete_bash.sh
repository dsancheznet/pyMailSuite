#/usr/bin/env bash
#Move this script to the directory /etc/bash_completion.d

_mailto() {

  local IFS=$'\n'
  TMPWORDLIST=$(~/Documentos/Code/Python-Code/pyMailSuite/addressbook --search=${COMP_WORDS[1]})
  COMPREPLY=($(compgen -W '$TMPWORDLIST'))

}

complete -F _mailto mailto
