# Attendance Program V2.0 demo

### 特性

- 基于 API 加载程序，支持配置功能修改
- 支持多种一言接口，基于 HTML UI 美化页面

## 使用

### 目录结构

```shell
│+--.idea
      +--flaskProject.iml
      +--inspectionProfiles
            +--profiles_settings.xml
            +--Project_Default.xml
      +--jsLibraryMappings.xml
      +--misc.xml
      +--modules.xml
      +--webResources.xml
      +--workspace.xml
+--filedir.py
+--LICENSE
+--README.md
+--考勤程序V2.0
      +--0-说明文档和配置文档
            +--说明文档.txt
            +--配置文档.txt
      +--1-学生名单表
            +--2楼学生名单.xlsx
            +--5楼学生名单.xlsx
            +--学生名单.xlsx
      +--2-考勤结果
            +--点名文档.txt
            +--考勤总表.xlsx
      +--favicon.ico
      +--Lenovo c-cay attendance.py
      +--程序源码
            +--data
                  +--excel.py
                  +--images.py
                  +--others.py
                  +--rdata.py
                  +--rdate.py
                  +--__init__.py
            +--main.py
            +--static
                  +--assets
                        +--autoload.js
                        +--flat-ui-icons-regular.eot
                        +--flat-ui-icons-regular.svg
                        +--flat-ui-icons-regular.ttf
                        +--flat-ui-icons-regular.woff
                        +--live2d.js
                        +--waifu-tips.js
                        +--waifu-tips.json
                        +--waifu.css
                  +--CommandBeeNest V1.7.lua
                  +--css
                        +--animate.min.css
                        +--aos.css
                        +--bootstrap
                              +--bootstrap-grid.css
                              +--bootstrap-reboot.css
                              +--bootstrap.css
                              +--mixins
                                    +--_forms.css
                                    +--_lists.css
                                    +--_pagination.css
                                    +--_text-truncate.css
                        +--bootstrap-datepicker.css
                        +--bootstrap.min.css
                        +--fancybox.min.css
                        +--index.css
                        +--jquery-ui.css
                        +--magnific-popup.css
                        +--mediaelementplayer.css
                        +--owl.carousel.min.css
                        +--owl.theme.default.min.css
                        +--students_manage.css
                        +--style.css
                        +--考勤页面.css
                  +--favicon.ico
                  +--fonts
                        +--flaticon
                              +--backup.txt
                              +--font
                                    +--flaticon.css
                                    +--Flaticon.eot
                                    +--flaticon.html
                                    +--Flaticon.svg
                                    +--Flaticon.ttf
                                    +--Flaticon.woff
                                    +--Flaticon.woff2
                                    +--_flaticon.scss
                              +--license
                                    +--license.pdf
                        +--icomoon
                              +--demo-files
                                    +--demo.css
                                    +--demo.js
                              +--demo.html
                              +--fonts
                                    +--icomoon.eot
                                    +--icomoon.svg
                                    +--icomoon.ttf
                                    +--icomoon.woff
                              +--Read Me.txt
                              +--selection.json
                              +--style.css
                  +--gotop.png
                  +--images
                        +--cls_imgs
                              +--lenovo_1.jpeg
                              +--lenovo_10.jpeg
                              +--lenovo_11.jpeg
                              +--lenovo_12.jpeg
                              +--lenovo_14.jpg
                              +--lenovo_15.jpg
                              +--lenovo_16.jpg
                              +--lenovo_17.jpg
                              +--lenovo_18.jpg
                              +--lenovo_19.jpg
                              +--lenovo_2.jpeg
                              +--lenovo_20.jpg
                              +--lenovo_21.jpg
                              +--lenovo_3.jpeg
                              +--lenovo_4.jpeg
                              +--lenovo_5.jpeg
                              +--lenovo_6.jpeg
                              +--lenovo_7.jpeg
                        +--hero-min.jpg
                        +--img_1.jpg
                        +--img_10.jpg
                        +--img_11.jpg
                        +--img_12.jpg
                        +--img_13.jpg
                        +--img_14.jpg
                        +--img_2.jpg
                        +--img_3.jpg
                        +--img_4.jpg
                        +--img_5.jpg
                        +--img_6.jpg
                        +--img_7.jpg
                        +--img_8.jpg
                        +--img_9.jpg
                        +--kaoqin_backgroud.jpg
                        +--lenovo.png
                        +--person_1.jpg
                        +--person_2.jpg
                        +--person_3.jpg
                        +--person_4.jpg
                        +--person_5.jpg
                        +--student_imgs
                              +--付一鸣.jpeg
                              +--叶平.jpeg
                              +--吕梦丽.jpeg
                              +--吴俊岳.jpg
                              +--孙佳奇.jpg
                              +--崔昊元.jpeg
                              +--张子豪.jpg
                              +--张阔.jpeg
                              +--李蓉轩.jpeg
                              +--牛皓冬.jpg
                              +--王孝天.jpg
                              +--王浩羽.jpeg
                              +--贾靖程.jpg
                              +--赵鑫博.jpg
                              +--郑佳睦.jpg
                              +--陈观绅.jpg
                  +--js
                        +--aos.js
                        +--bootstrap-datepicker.min.js
                        +--bootstrap.min.js
                        +--jquery-3.3.1.min.js
                        +--jquery-3.4.1.js
                        +--jquery-migrate-3.0.1.min.js
                        +--jquery-ui.js
                        +--jquery.countdown.min.js
                        +--jquery.easing.1.3.js
                        +--jquery.fancybox.min.js
                        +--jquery.magnific-popup.min.js
                        +--jquery.min.js
                        +--jquery.stellar.min.js
                        +--kaoqin.js
                        +--lozad.min.js
                        +--main.js
                        +--mediaelement-and-player.min.js
                        +--owl.carousel.min.js
                        +--popper.min.js
                        +--slick.min.js
                        +--typed.js
                  +--lua.lua
                  +--prepros-6.config
                  +--scss
                        +--bootstrap
                              +--bootstrap-grid.scss
                              +--bootstrap-reboot.scss
                              +--bootstrap.scss
                              +--mixins
                                    +--_alert.scss
                                    +--_background-variant.scss
                                    +--_badge.scss
                                    +--_border-radius.scss
                                    +--_box-shadow.scss
                                    +--_breakpoints.scss
                                    +--_buttons.scss
                                    +--_caret.scss
                                    +--_clearfix.scss
                                    +--_float.scss
                                    +--_forms.scss
                                    +--_gradients.scss
                                    +--_grid-framework.scss
                                    +--_grid.scss
                                    +--_hover.scss
                                    +--_image.scss
                                    +--_list-group.scss
                                    +--_lists.scss
                                    +--_nav-divider.scss
                                    +--_pagination.scss
                                    +--_reset-text.scss
                                    +--_resize.scss
                                    +--_screen-reader.scss
                                    +--_size.scss
                                    +--_table-row.scss
                                    +--_text-emphasis.scss
                                    +--_text-hide.scss
                                    +--_text-truncate.scss
                                    +--_transition.scss
                                    +--_visibility.scss
                              +--utilities
                                    +--_align.scss
                                    +--_background.scss
                                    +--_borders.scss
                                    +--_clearfix.scss
                                    +--_display.scss
                                    +--_embed.scss
                                    +--_flex.scss
                                    +--_float.scss
                                    +--_position.scss
                                    +--_screenreaders.scss
                                    +--_shadows.scss
                                    +--_sizing.scss
                                    +--_spacing.scss
                                    +--_text.scss
                                    +--_visibility.scss
                              +--_alert.scss
                              +--_badge.scss
                              +--_breadcrumb.scss
                              +--_button-group.scss
                              +--_buttons.scss
                              +--_card.scss
                              +--_carousel.scss
                              +--_close.scss
                              +--_code.scss
                              +--_custom-forms.scss
                              +--_dropdown.scss
                              +--_forms.scss
                              +--_functions.scss
                              +--_grid.scss
                              +--_images.scss
                              +--_input-group.scss
                              +--_jumbotron.scss
                              +--_list-group.scss
                              +--_media.scss
                              +--_mixins.scss
                              +--_modal.scss
                              +--_nav.scss
                              +--_navbar.scss
                              +--_pagination.scss
                              +--_popover.scss
                              +--_print.scss
                              +--_progress.scss
                              +--_reboot.scss
                              +--_root.scss
                              +--_tables.scss
                              +--_tooltip.scss
                              +--_transitions.scss
                              +--_type.scss
                              +--_utilities.scss
                              +--_variables.scss
                        +--style.scss
                        +--_site-base.scss
                        +--_site-blocks.scss
                        +--_site-navbar.scss
                  +--students_introduction.json
            +--templates
                  +--01-live2d-master.html
                  +--02-live2d-master-default.html
                  +--03-live2d-master-autoload.html
                  +--04-live2d-master-waifu-tips.html
                  +--exam.html
                  +--index.html
                  +--root.html
            +--utils
                  +--EnglishWordsTest.py
                  +--configure.py
                  +--illustrate.py
                  +--__init__.py
```

### 食用方法

- 依赖类库
  - Python OS (`lb-main.py`)
  - Flask UI (仅实现 *考勤功能*)

## 版权声明

> 未来联想班 - 萝卜开发组 ( ˃ ˄ ˂̥̥ ) 都看到这了，点个 Star 吧 ~
> Mysql 服务端 https://c-acy-attendance.com/


[Flat UI Free][1]  
[Lenovo / ©journey-lb / GPL v2.0][2]  
[lb-main.py / ©journey-lb / CC BY-NC-SA 2.0][3]  
  
Open Attendance Program V2.0 license.


  [1]: https://designmodo.com/flat-free/ "Flask UI Free"
  [2]: https://github.com/journey-ad/live2d_src "基于 #Qr_por 的修改版"
  [3]: https://imjad.cn/ "萝卜开发组"
