(add-to-list 'load-path "d:/home/emacs-24.1/site-lisp/slime/")
(setq inferior-lisp-program "d:/home/emacs-24.1/bin/clisp/clisp.exe")
(load "d:/home/emacs-24.1/site-lisp/wsz/wsz.el")
;; (set-cursor-color "white")   
;; 鼠标颜色设置为白色   
;; (set-mouse-color "white")   
;; 设置背景颜色和字体颜色   
;; (set-foreground-color "white")   
;; (set-background-color ";; darkblue")   
;; 设置另外一些颜色：语法高亮显示的背景和主题，区域选择的背景和主题，二次选择的背景和选择   
;; (set-face-foreground 'highlight "white")   
;; (set-face-background 'highlight "blue")   
;; (set-face-foreground 'region "cyan")   
;; (set-face-background 'region "blue")   
;; (set-face-foreground 'secondary-selection "skyblue")   
;; (set-face-background 'secondary-selection "darkblue")   
;;设置日历的一些颜色   
;; (setq calendar-load-hook   
    ;; '(lambda ()   
    ;; (set-face-foreground 'diary-face "skyblue")   
    ;; (set-face-background 'holiday-face "slate blue")   
    ;; (set-face-foreground 'holiday-face "white"))) 
(require 'python-mode)
(add-to-list 'auto-mode-alist '("\\.py'" . python-mode))
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
(require 'auto-complete)
(require 'auto-complete-config)
(global-auto-complete-mode t)
(setq-default ac-sources '(ac-source-words-in-same-mode-buffers))
(add-hook 'emacs-lisp-mode-hook (lambda () (add-to-list 'ac-sources 'ac-source-symbols)))
(add-hook 'auto-complete-mode-hook (lambda () (add-to-list 'ac-sources 'ac-source-filename)))
(set-face-background 'ac-candidate-face "lightgray")
(set-face-underline 'ac-candidate-face "darkgray")
(set-face-background 'ac-selection-face "steelblue") ;;; 设置比上面截图中更好看的背景颜色
(define-key ac-completing-map "\M-n" 'ac-next)  ;;; 列表中通过按M-n来向下移动
(define-key ac-completing-map "\M-p" 'ac-previous)
(setq ac-auto-start 2)
(setq ac-dwim t)
(define-key ac-mode-map (kbd "M-TAB") 'auto-complete)
(require 'org-install)
(add-to-list 'auto-mode-alist '("\\.org$" . org-mode))
(define-key global-map "\C-cl" 'org-store-link)
(define-key global-map "\C-ca" 'org-agenda)
(setq org-log-done t)
(setq org-todo-keywords '((sequencep "TODO" "正处理" "待废弃" "|" "DONE" "已废弃")))
(setq org-agenda-files (list "~/org/work.org"
                             "~/org/home.org"
			     "~/org/java.org"
			     "~/org/learn.org"))
(setq org-default-notes-file "~/.notes")
;;日期
(setq display-time-24hr-format t)
(setq display-time-day-and-date t)
(display-time)
;;TODO 模式
(setq todo-file-do "~/emacs/todo/do")
(setq todo-file-done "~/emacs/todo/done")
(setq todo-file-top "~/emacs/todo/top")
(setq diary-file "~/emacs/diary")
(setq diary-mail-addr "ivyicy@qq.com")
(add-hook 'diary-hook 'appt-make-list)
;;打开约会提醒功能
(setq appt-issue-message t)
;;绑定快捷键
(global-set-key [(f9)] 'list-bookmarks)
(global-set-key [(f12)] 'org-remember)
(global-set-key [(f11)] 'calendar)
(global-set-key [(f10)] 'todo-mode)
(global-set-key [(control \?)] 'comment-line-or-uncomment-it)
(global-set-key [(meta ?/)] 'hippie-expand)   
(setq hippie-expand-try-functions-list   
      '(try-expand-line   
	try-expand-line-all-buffers   
	try-expand-list   
	try-expand-list-all-buffers   
	try-expand-dabbrev   
	try-expand-dabbrev-visible   
	try-expand-dabbrev-all-buffers   
	try-expand-dabbrev-from-kill   
	try-complete-file-name   
	try-complete-file-name-partially   
	try-complete-lisp-symbol   
	try-complete-lisp-symbol-partially   
	try-expand-whole-kll))
;;禁用启动画面
(setq inhibit-startup-message t)
;;尺寸
(setq initial-frame-alist '( (width . 90) (height . 35)))
;;高亮显示成对括号
(show-paren-mode t)
(setq show-paren-style 'parentheses)
(linum-mode t)
(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(safe-local-variable-values (quote ((todo-categories "异常" "正常" "java")))))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 )
(put 'upcase-region 'disabled nil)
