#lang s-exp framework/keybinding-lang
(keybinding "c:a" (λ (editor evt) (send editor insert "!")))
(keybinding "d:]" (λ (editor evt) (send (send editor get-keymap) call-function "uncomment" editor event #t)))