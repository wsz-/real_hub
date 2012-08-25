(add-to-list 'load-path "d:/home/emacs-23.4/site-lisp/slime/")
(setq inferior-lisp-program "d:/home/emacs-23.4/bin/clisp/clisp.exe")
(require 'slime)
(slime-setup)
;;Emacs23 for windows ��������
(setq w32-charset-info-alist
(cons '("gbk" w32-charset-gb2312 . 936) w32-charset-info-alist))
(setq default-frame-alist
(append
'((font . "fontset-gbk")) default-frame-alist))
(create-fontset-from-fontset-spec
"-outline-Courier New-normal-r-normal-normal-13-927-96-96-c-*-fontset-gbk")
(set-fontset-font
"fontset-default" nil
"-outline-������-normal-r-normal-*-14-*-96-96-c-*-iso10646-1" nil 'prepend)
(set-fontset-font
"fontset-gbk" 'kana
"-outline-������-normal-r-normal-*-14-*-96-96-c-*-iso10646-1" nil 'prepend)
(set-fontset-font
"fontset-gbk" 'han
"-outline-������-normal-r-normal-*-14-*-96-96-c-*-iso10646-1" nil 'prepend)
(set-fontset-font
"fontset-gbk" 'cjk-misc
"-outline-������-normal-r-normal-*-14-*-96-96-c-*-iso10646-1" nil 'prepend)
(set-fontset-font
"fontset-gbk" 'symbol
"-outline-������-normal-r-normal-*-14-*-96-96-c-*-iso10646-1" nil 'prepend)
(set-default-font "fontset-gbk")
(require 'python-mode)
(add-to-list 'auto-mode-alist '("\\.py'" . python-mode))
;;Code highlighting produced by Actipro CodeHighlighter (freeware)http://www.CodeHighlighter.com/-->(require 'auto-complete)
;(require 'auto-complete-config)
;(global-auto-complete-mode t)
;(setq-default ac-sources '(ac-source-words-in-same-mode-buffers))
;(add-hook 'emacs-lisp-mode-hook (lambda () (add-to-list 'ac-sources 'ac-source-symbols)))
;(add-hook 'auto-complete-mode-hook (lambda () (add-to-list 'ac-sources 'ac-source-filename)))
;(set-face-background 'ac-candidate-face "lightgray")
;(set-face-underline 'ac-candidate-face "darkgray")
;(set-face-background 'ac-selection-face "steelblue") ;;; ���ñ������ͼ�и��ÿ��ı�����ɫ
;(define-key ac-completing-map "\M-n" 'ac-next)  ;;; �б���ͨ����M-n�������ƶ�
;(define-key ac-completing-map "\M-p" 'ac-previous)
;(setq ac-auto-start 2)
;(setq ac-dwim t)
;(define-key ac-mode-map (kbd "M-TAB") 'auto-complete)
(autoload 'pymacs-apply "pymacs")
(autoload 'pymacs-call "pymacs")
(autoload 'pymacs-eval "pymacs" nil t)
(autoload 'pymacs-exec "pymacs" nil t)
(autoload 'pymacs-load "pymacs" nil t)
(require 'pycomplete)
(setq auto-mode-alist (cons '("\\.py$" . python-mode) auto-mode-alist))
(autoload 'python-mode "python-mode" "Python editing mode." t)
(setq interpreter-mode-alist(cons '("python" . python-mode)
                           interpreter-mode-alist))
(put 'upcase-region 'disabled nil)
(global-set-key "\C-x\C-m" 'execute-extended-command)
(global-set-key "\C-c\C-m" 'execute-extended-command)
(global-set-key "\C-w" 'backward-kill-word)
(global-set-key "\C-x\C-k" 'kill-region)
(global-set-key "\C-c\C-k" 'kill-region)
(require 'org-install)
(add-to-list 'auto-mode-alist '("\\.org$" . org-mode))
(define-key global-map "\C-cl" 'org-store-link)
(define-key global-map "\C-ca" 'org-agenda)
(setq org-log-done t)
(setq org-todo-keywords '((sequencep "TODO" "������" "������" "|" "DONE" "�ѷ���")))
(setq org-agenda-files (list "~/org/work.org"
                             "~/org/home.org"
			     "~/org/java.org"))
(custom-set-variables
  ;; custom-set-variables was added by Custom.
  ;; If you edit it by hand, you could mess it up, so be careful.
  ;; Your init file should contain only one such instance.
  ;; If there is more than one, they won't work right.
 '(Org-agenda-files (quote ("~/org/work.org" "~/org/home.org" "~/org/java.org"))))
(custom-set-faces
  ;; custom-set-faces was added by Custom.
  ;; If you edit it by hand, you could mess it up, so be careful.
  ;; Your init file should contain only one such instance.
  ;; If there is more than one, they won't work right.
 )
(setq org-default-notes-file "~/.notes") 
;;����
(setq display-time-24hr-format t)
(setq display-time-day-and-date t)
(display-time)

(setq todo-file-do "~/emacs/todo/do")
(setq todo-file-done "~/emacs/todo/done")
(setq todo-file-top "~/emacs/todo/top")

(setq diary-file "~/emacs/diary")
(setq diary-mail-addr "you@your.email.address")
(add-hook 'diary-hook 'appt-make-list)
;;��Լ�����ѹ���
(setq appt-issue-message t)
;;�󶨿�ݼ�
(global-set-key [(f9)] 'list-bookmarks)
(global-set-key [(f12)] 'org-remember)
(global-set-key [(f11)] 'calendar)
(global-set-key [(f10)] 'todo-mode)
;;cedit
(require 'cedet)
(global-ede-mode t)
;;Helper tools.
(custom-set-variables
'(semantic-default-submodes (quote (global-semantic-decoration-mode 
				    global-semantic-idle-completions-mode
				    global-semantic-idle-scheduler-mode
				    global-semanticdb-minor-mode
				    global-semantic-idle-summary-mode
				    global-semantic-mru-bookmark-mode)))
'(semantic-idle-scheduler-timer 3))
(semantic-mode)
;; smart complitions
(require 'semantic/ia)
(setq-mode-local c-mode semanticdb-find-default-throttle
                 '(project unloaded system recursive))
(setq-mode-local c++-mode semanticdb-find-default-throttle
                 '(project unloaded system recursive))
;;;;  �������߲���
;;; hippie-try-expand settings
(setq hippie-expand-try-functions-list
      '(
        yas/hippie-try-expand
        semantic-ia-complete-symbol
        try-expand-dabbrev
        try-expand-dabbrev-visible
        try-expand-dabbrev-all-buffers
        try-expand-dabbrev-from-kill
        try-complete-file-name-partially
        try-complete-file-name
        try-expand-all-abbrevs))

(defun indent-or-complete ()
  "Complete if point is at end of a word, otherwise indent line."
  (interactive)
  (if (looking-at "\\>")
      (hippie-expand nil)
    (indent-for-tab-command)
    ))

(defun yyc/indent-key-setup ()
  "Set tab as key for indent-or-complete"
  (local-set-key  [(tab)] 'indent-or-complete)
  )