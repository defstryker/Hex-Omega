from django.http import HttpResponse

dat = """<body style="background-color: black; color: white;padding: 5% 30%; font: 30px monospace;">"""""
dat += """<pre style="font: 10px/5px monospace;">;''++++++++++++++##########++++++++++++++++'';'+''''++++++'+'++++++'''''+++++++++++++#+########''''+######''+++''+++'
'+++++++++++++#####################+++'+';'++++++#####++++''+++''++++++++++#+++###############@###++++###@#++##++++++
'''''''''++++++++################+++'';;'''';;;;;';;;;;;;;;;''''+''+++++##++#++++#############@@@@########@####++++++
'''''''''''++++++++++++++++++++''';;;''++++'''''+++''';;;;;;::;;'''''+++++######+++##############@@###+##++#@@@##++++
''''''''''''''++++++++++++++++''''''''''''''''''''';;;;';;;;;;;;;;''+'''++++#####+++##############@@@@@@@@###@@@@#+++
'++''+''''''''''''''''''''';'++++++++'+++''+'+'''';';';;;;;;;;;;;::'''''''+++++####+++##########@@@@@@@@@@@@###@@@#++
++++++++''''''''''''''+';''++++++++''+''''''''''''''';;;;;;;;;;;;;;:;;'''''+'+++++####++#############@@@@@@#@@@@@@@##
'++++++++''''''''''''';'''''+'++++++''+++''''''''';;;;;;;;;;;;;;;;;;:::;''''++'+++####++++###########@@@@@@@++#@@@###
++#+++++++++'''''';;''''''''''''''''''''''''''+''';;;;;;;;;;;;;;;;;;;;;;;;;'+'''''++###++'++##########@@@@@@@#+@@####
+###++++++''++''';'''''''';;;;;''''''''''''''';;;;;;;;;;;;;;;;;;;;;;;;;;;'';''''''+++###++''+++########@@@@@@@@#@@@##
+#####+++++++'''''''''';;;;''''''''''''''''';;;;;;;;;;;;;;;;;;;;;;;;;;;;;''';'''''+++##++++++''++#######@@@@@@@#@@@##
+#####++++++''''''''';;;''''''';;''''''';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;'''';''''''+##+#+++++''+++######@@@@@@@##@#@
++####+++++'++'''''''''''';;;;''''''';;;;;;;;;;;;;;;:::;;;;;;;;;;;;;;;;;;'''';;''''+'+++###++++''+++######@@@@@@@##@@
'+####'+#++++'';''''+'''';;'''''';;;;:;;;;;;;;;;;::::::;;;;;;;;;;;;;;;;;;;;';;;;'+++'++++##+++#+++#+######@@@@@@@@##@
+++++'+#+++''+++++++'+++''''''';;;::;;;;;;;;;;;:::::::::;;;;;;;;;;;;;;;;;;;;;;;;'+'''+++++++++++'+##+'+###@@@@@@@@@@@
'++''+++++;'++++++'+++''''''';;:::;;;;;;;;;;;;::::::::::;;;;;;;;;;;;;;;;;;;;;;;;;;''';+++++++++#+'+##++'++###@@@@@@@@
'+''+++++;++++++++++++++'''';:::::;;;;;;;;;;::::::::::::;;;;;;;;;;;;;;;;;;;;;;;;;;;''+'''+++++++##'+#+++++###@@@@@@@@
'''++'++;+++++'+++++++''''';:::::;;;;;;;;;;;:::::::::::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;'''+''''++++++#+###+++#####@@@@@@
''''''';'+++++++++++'''''':;:;;:;;;;;;;;::;;:::::::::::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;''++'++++#+++#+####+++###@@@@@@
;'''';;'''+'+++++++++''';;:;;;:;;;;;;;;;;;;::::::::::::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;'+'++++++++++'+##++'#####@@@@
;'';;;;'''''+++++++''';;;;;;;;;;;;;;;;;;;:::::::::::::;;;;;;;;;:;;;;;;;;;;;;;;;;;;;;;;;;;'''+++++#++#+'###++'###@@@@@
;;;;':;;'''+++''+'''':;;;;;;;;;;;;;;;;;;;:::::::::::::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;'';;;;'''++'+#++##+'###++++##@@##
;;;';;;;;;'''''''''':;;;;;;;;;;;;;;;;;;;;::::::::::::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;';;;;;;'''+++++#####++#+++#+###@#
;';;:;;;;''';''''':;;;;;;;;;;;;;;;;;;;;;;:::::::::::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;''++++######++###+####@@
;';;:;;;;;;;;''';:::;;;;;;;;;;;;;;;;;;;;;::::::::::::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;';;';;;;;''+++#######++++#####@@
;';;;;;;;;;;;;;;;:::;;;;;;;;;;;;;;;;;;;;::::::::::::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;';;;;'';'++++########+'#+####@
';;;;;;;;:;;;;;;;::::;;;;;;;;;;;;;;;;;'++#;::::::::::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;'';;;;;'''''++++#########+###@@@
';;'';;;;;;;;::;;:::::;;;;;;;;;;:;:;''++#+##+::;::::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;'';;;;;;''''''++++#########++##@@
;''';;;;;;;;:::;::::::;;;;;;;;;;:::;;+'+++'+@'::::::;;;;;;;:;;;;;;;;;;;;;;;;;;;;;;;;;;;';;;;'''''''++++#########++#@@
;''';;;;;;;:;:::::::::::;;;;;;:::,;;;''++;;;+#'::::;;;;;;;;;:::;;;;;;;;;;;;;;;;;;;;;;;';;;;;''''''''+++++########+#@@
;''';';';;:;::::,,::::::::;:::::,:+,;'++'+:;;##:::;;;;;;;;;;:::;;;;;;;;;;;;;;;;';;;;;;';;;;;;';''''+''++#########++@@
;''''''';;;;:::,,,,::::::::::::,;;,,'''+''+;:@#:;;;;;;;;;;;::::;;;;;;;;;;;;;;;;';;;;;;';;;;;;;;'''''++'++#########'#@
'''''''';;;;:::,,,,,:::::::::::;;':':.;'#'';:@+;;;;;;;;;;;:;:::;;;;;;;;;;;;;;;;;;';;;;;;;;;;;;'''''+++#'+++#######++#
''''++'''';;;::,,,,,:::::::::,;;++;;..,;;;;'#@@';;;;;;;;;;::::::;;;;;;;;;;;;';;'';;;;;;;;;;;;;'''';'++##'+'+#######++
'+++++'''';;;:::,,,,,,,::::::;;'+'+...,;;;.'+@##';;;;;;;;;::::::;;;;;;;;;';;;;''';;;;;;;;;;;;'''';;++++##++++#######+
'++++'''';;;;::::,,,,,,,,::::;;'+#;`,,,;;;,'#####;;;;;;;;;:::::;;;;;;;;;;;;;''''';;;;;;;;;;;;;'';;;'+++##+++'+######+
''++'+'''';;::::::,,,,,,,,,:;:;+##:`..:'''';@@@#+#;;;;;;;;:::::;;;;;;;;;;;'''';'';;;;;;;;;;;;;';;;;'++++##+++++######
'++++'''''';:::::::,,,,,,,,,,'+###:..,:;'+;+@@#@@';;;;;;;;:::::;;;;;;;;;;''''''';;;;;;;;;;;;;;;;;;;''++++##+++++#####
'++++''+'';;;::::::,,,,,,,,;;++##',,..,;''+@######+;;;;;;:::::;;;;;;;;;;'''''';;;;;;;;;;'';;;;;';;;''++++###+'+####+#
++++'++''';;;;::::::,,,,,,:;;+'#+::,,::;;+@@##@@##+;;;;;:::::::;;;;;;;;'';;'';;;;';;;;;;';;;;;;';;';;++'++###+'+####+
+''''+''';;;;;::::::,,,,,:,'''++#`:,;'';#@#@####@##';;:::::::::;;;;;;;;;;;'';;;;;';;;;;';;'';;;;;;;;;'+'++####++###+#
+''++''';;;;;;:::::::,,,,:+'+++++.,:'''#@@@##++;##++;;:::::::::;;;;;;;;;;';;;;;;;';';;';'''';;'';;;;;+''++####++++###
''''+'';;;;:;::::::::,,,;'+++++;.::;''+@@@##+#'#+##''::::::::::;;;;;;;;;;;;;;;;;;''';;;;';';'';';;;;;'+++'++####'+###
;'+''';;::::::::::::::,,' .:'+;`..:,##+####+#++#;++#';:::::::::;;;;;;;;;;;;;;;;;;'';;;''';';;'';';;;;''++'+++###+++##
;'''';;::::::::::::::::;..:;''',,`.;+''##+##+##+'''+#';:::::::::;;;;;;;;;;;;;;;;;'';;;;;';;;';;;';;;;''''+'++####+++#
;''''':::::::::::::::::; .;'''';,..:''##+###+#'''#+:'+:;;;;:::::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;';;;;;'+'+''++###++++
'''';::::::::::::::::::;`,;''';;,.,::+#+++##++'''#+:+#;::::::::::;;;;;;;;;;;;;;;;;;;;;;;;';;;;;;';;;;;;'''+'++###+++#
;'';;::::::::::::::::::,`,;'';::..:,;++#####;'''''::'+';::::::::;;;;;;;;;;;;;;;;;;;;::;;;';;;';;';';;;:''++''+###+++#
;';;::::::::::::::::::: `,:;;:,,,,:;++###@@+'+'+++:;;+;;::::::::;;;;;;;;;;;;;;;;;:;;:;:;;';;;;;;;';;;;:''++'+++###'+#
;;;::::,,:::::::::::::; `,:';,,,,,;'+#+##@@#'+++#;:':':;;;;:::::;;;;;;;;;;;;;;;::;;;:::;;';;;;;;;';;;;;'++''++++##++#
;;::::,,,::::::::::::::..,;'',,,,:'++@+#'@#@#'+#'::::;'::::::::::;;;;;;;;;;;;::::::;::;;;;;;;;;;;';;;;;;++'+++++##+++
;;:::,,,,,::::::::::::;:,;''':,,,'+###;+;@#@+'''';::::;::::::::::::;;;;;;;;::::;;::;::;;;;;;;;;;;';;;;;:''''+'++#+++#
;;::,,,,,,::::::::::::'',;++''..+;##@;+;+@+'+#'';';:::::::,,,:::::::;;;;;;:::;;;;::;:::;;;;;;;;;;':;;;;:''''+'+#+#++#
;::,,,,,,,,,,,,,:::::,:;.;++''`''++@':;'#@##;++''':::::::,,,,,::::::::::::;;;;:;;;;::;;;;;;;;;;;;;;;;;;:'+''+++###+++
::,,,,,,,,,,,,,,,,,,:`.:.;'+''.`'###';`;++@';+#'''':,:::,,,,,,,,:::::::::;;:;;;:;;;;;;;;;;;;;;;;;;;;;;;:''''+#++##'##
:::,,,,,,,,,,,,,,,,,,` ,,;'';'':+#++''.:;##@+''+'';;,::::,,,,,,,,::::::::;;;;;;;:;;;;;;;;;;;;;;;;;;;;;;:;'''+##+##'##
:::,,,,,,,,,,,,,,,,,,``.:'';;'`'#++''',.;;@##;'#'';;,,:::,,,,,,,,,,::::::;;;;;;;;:;;;;;;;;;;;;;;;;;;::;;;';'++++#+'##
:;::,,,,,,,,,,,,,,,,, .,;';::; ;##'''';.,;##+;++''':,,.,,,,,,,,,,,,,,,,:::::;;;;;:;::;;;;;:::;;;:::::;;':''++++#+'+##
:;::,,,,,,,,,,,,..... .`,':::;`'+#''''',,;;##;#+''';,:,,,,.,,,,,,,,,,,,,,,:::::;::::::::::::::::::::;;''';'+#++#+;###
;;;::,,,,,,,,........ ..;,,,,:.+##';;;;':;'+#;#+'''':++'';;;';,,,,,,,,,,,,,:::::::::::::::::::::::::;;'::+'+#++#'++##
;;::::,,,,,,........``.:;.,.,,:++#';;;''''''#'+++';';+++'+'';::::,.,,,,,,,,,:::::::::::::::::,:,,:;;;'',''+++++#''+##
;;;:::,,,,.......... ..::..,.,:;+++;;;''''++#++';;;':++++''';:::::,,.........,,,,,,,,,,,,,,,,,,,,::;''':'++++++#;''++
;;;:::::,,.........` ,,,:.`.,,,''#;';'''''++'+':::'';+###;'';+''++';..........,,,,,,,,,,,,,,,,,,:;;;;'':'+++'+##'''++
;';;:::::,,........ `,.;,,``,,,,+';'''''''+++':::;'';##+''''++####++',.........,,,,,,,........,:;;;;''+;'+''+##+''''+
:::,,....``.....``` `,:'...`,,..,;;'';''''++;::;;'''+#++'+++++'#'#+##+,........,...............,,::::::;';++++++:'+++
,,,,,..............``,;:..,` ,,,,'+:'';;''+,,:;;;'''#+++#+''+'';''+##++;.,,,,..................::':,,,,;''+++++''++++
,,,,.......`...... `.;;;..,,.`,,,,;:;''''';,;:;;'++######++++''';:;;####;,.....,,,.,,,,,,,,,.:';'';':,+++++++++;+++++
;,,,,,,,,,,,,,,,,, `,;;,...,,.,...,.:;''':..;;''+'#+###@#+#++++;;;;;+++##+',,,,,,,,,,,,,,,,,,,,:::::::,,:;'''':'++++'
+;::,,,,.....,,,,,`..';....,,,`,,,,,,,,.;`.:;;'+'++@#@@##+#+#+';',:,'++++##++::::::,,,,,,,,,,,:::::::::;;''''''''';''
'+':,,,,,,,,:::,,,`,;;;,....,,.,:::,,,,,`.:''++'+#@#@#@####+++++;;''':'++#+##++;::::::::::::::;:;;;;;;;;;'''''''+++++
;';;;;::::::::::, `:;'::,,..`.,.:,::::: .,;'''++'##@##@#####+#++''';::+;'++++###++++';;::::::;;;;;;;;;''''''''''+++++
'+++''';;;;;;::::`.;'';:,,,:,.,.,,,,::`.,:'''+''+#@@#@#@#'####+#+';:';;:+++'#++##+#++#'#++'';:::;;;;;;:;;;;;''''+++++
++'''''''''';;;;;.,'';:;,,,.,..,.,,.,.`,;;''++'+#########+######++''':'''''++++##+++##+#+'@#####+';;;;;;;;;'''''''''+
+++''''''''';;;;`.:'';:;;::,,:,,,,., ..;''';+'+'@@@@@#@#+@+#####++++++'''+++''+#'#+''+###+##########+';;''''''''''+++
+++''';;;;;;;:::.::';:;::;::,::::::.,,;'';;;;'++@@@@@@@@##@######+#+++++++#+#+#+#+++++++#++++#++#######+;;;'''''''+++
''''''';;;;::::`.:'';::::::,:,,:::;..:;;;:';;;##@@@@@@@#@+@#@##@@####++##+#+#+#+#+++++++++'+'+'+'+++##@##+;';;;;;''''
'+'''''';;;;;;. .'+',::::...,:::::..::;;:,';::'#@@@@@@@@@##@@#@@@#@#+####+######@##+######+#+++''''+'#+####''''''''++
''''''';;;;::.`.:'';:::,;:,,,,;;'::,.;;':,;':::'@@@@@@@@@#@@@@@@#@#####@#####@###@#@#@@#@#####+#''+''+++@##+''''''+++
'''''''':.`,` `.;'+'';';,::;:;;.:;;;.;;+''';::::'@@@@@@@@#@@@@@@@@@@@@@#@#@@@@@#@@@@@#@@@@@@###+++';+''#####+''''''''
'''';':...,. .:,,;'''''''':;,:.;',;:,;''+'':,:;;++#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+@+#+#''''+###++'''''++
''';:...:.',.,:;''';;;:;;;;..;.:'+:+:;''+'+'+;;;+++##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###+''''++####+;;;;;''
'''',::;`,@.'+':;''';;';,:::,:+##,'#;;+'+'+++';'+++#+###@@@@@@@@@@@##++++++##@@@@#@@@@@@#@@@@@@@@##+++;+'+####+''''''
'';,;;;`;+.++++';';;++;.:;+++++#;+#+';''+'+++''+++#####+###@@@#'::'+++#######+';;'##@###@#@@###@@###'';'+##@###;;''''
;:,,:;.'+`'++++'''''',,:;'++;'+######'';''+++';+####++#+###+:;+######+###@@@@@@@@##';+###########@##+':''+##@##''''''
;:;':,;++';';''+++++.,,:+++'+++#####@@+;'++'++'+#########,;+######@@@@@@@@@@@@@@@@@@@#+'#####+++###+':''###@@@#+';';;
::'':;';''++++'++#'::;;;+++'+++++##@@#'+;++++'+#######+,+#####@@@###++###@@@@@@####@@@@@#;+++++#++#'''''###@@##'++'''
;';;'''+++++###+':.,;'''+'++'++++++#####''+++++######.+###++@@######@@@@@@@@@@@@@@@@@@@@@@#''+++''';'''+####@#@+++';'
';'''+'+#######+':';'++''''''''++++####+#'''+''+###,'##++#@@###@@@#####@@@@@@#@@@@@@##@@@@@@@#+'';'+++++###@@@#+##';;
+++#'+########+;::'''++++'++++###+#####@#+'+'++'#':##++#@@++#@@##@@@###################@@@@@@@#+'''+++#########+##+++
+############+';,:;'+++++;++++########@@@@+#+'++,+#++#@@#+@@###@######@@@@@@#@@@@@@@@@@@@@@@@####++++#####@###++###++
+##+,.,,+####+':;''+++++'+++++#######@#''''+#+;:##++@@#+####@#####@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##########@@@##'####++
+++;,.,:;'##++''''+'++++++#++#++++'+##;:;''++,++#'@@#+#@#+##@##@@@##@@@@@@@@@@########@@@@@@@@@@@##@###@@@@@##+@#####
..+:;:,;;++#++'''#'++++#+####++#'+++#;:.:;'+`++++@##+@#+##@##@@###@@@@@@@####@@@@@@#@@@@@@@@@@@@@@@#@@#@@@###+#######
,.',;##';+##+++'++#++######+#+#++++++;::,:':++++##+#@#########@#@@@@@@@#@@##@@@@@@@@@@@@@@@@@@@@@#@@@@@@####++#@####@
,.,,'@##'###+++++''+########+###++++';::;;;+++#@++@#+##@####@##@@@@@@#@##@@@@@@@@@@@@@@@##@@@#@@@@#@@@#@####+#####@@#
+;;;;+#;++##++++''++######+;;;;++++++';;;'+++@#+#@#+######@@#@#@@@@#@#@@##@@@@@@@@@####@@@@@@@@@@#@@@@@###++++###@@++
''+#'''#+++#++++++##+'#',::;''+++'##+'+;''#'@#+###+#@####@@##@#+'###@#+'''@@#####@@@@@@@#@@@@@@@##@@@@###+'+++###@+##
+++@#++#+#+++++###',:::::''+''+++#+'++'''#+@#+###+@##+#@+@##'''+'#@+''''+####++#@@#@@##@@@@@@@@@#@@##@#+++++++###+++@
'+##+'''++''''''+:,,;,:;;''+++''+++##'''####+@@##@+'##++##+'''''@''''''++'''''''####@@@#@@@@@@@##@#####+++++++##'+#@+
;'+++++'';;;::::,:'';;;''++++++++#+++:'####+#####+'+#++'@+'''''#''''+++++''''''''#@@@#@@@@@@#@@#@#####''''+++##'+####
;';'++'';;;;;:,:;;;;''++++++++++++##:'@+##+#'###+'##'''@';;''';'''':''+++#+'''''''@#@@@@@@@@@@##@+#+#+'++;+++'++####+
;;;;;;;;;;;::,++'++'++++++#++++###+,+@+@#+#''#+'';+;;;';;;';'':''':,:;'+++#+''''''#@@@@#@@@@@#@@###++'+''''+++++++###
;;;;''';;;;:';''+''++#######+##++#,+@'@##+':;#:::+;;;;:;;'''''''':;;::''++##'''''''@@##@@@@@##@@###+++++++++''''++++#
;;;;:;:;;:,,,,,::++####+++++++++':'##@###':,#:::;::;;:;;;''''';'''#@';'''+##+''';'###@@@@@@@@@@#@#++'+++++++++++++++#
:;;;;::;:::::,:;;;;::;++++'''';:,;'+++;+';:;::;;;;;'''''''++++++++@@;'#@@#######+'#@@@@@@@@@@@@###++#++++++++++++++'+
;''''';;;;;::::;;'++++''''';:::,,,,:::::::;;';'''''''''''+++'+++;'#'@##@@#+##+++'#@@@@@@@@@@@@#@#++'+++###++###++#+++
:::;;;;;;;;;;;';;;;;;;;;;'''''':++''';+''';;;;';;''';''';''''''+:,:;##+@@+####+'@@@@@@@@@@@@@#@##+#+###########+###++
;;;;;;:::::::::;;;;;;;;;;::;;;:+#+++;'';;;;;;;'''';''''''';'';'+'':;''+'''##+'+##@@@@@@@#@@@#@#@##+++#+#####+#+++##++
;;;;;:,,,,,,,::;;;;;;'''''''';'''++;'';;;;'''';;;'''''''''';;'++++;;'++#++##+#+'+#+############++++##+@@###++++++++'+
;'''';;;;;;:::::::::::::;;;;;'#+;#;;#;;;;;;;;;;;;;;;;;''''''''';:;;'+++###++''''+++++++##++####+++++####+'+++++#+''++
;''';;'''''''''';;;;;''''''''++'+''';;;'''''''''''';;;;;''''''''++++'+;;;;'''+++#+##########++++####+'+++++++++''+++#
'+++++'''''';;;::;;;;;;;;;;'#+;#''''';';''''''''''''''';;;;;'';;+++++#@#+'''''''''''+++++++###++''++++++++++++++++#++
'++++++''''''''''''''''''+'#+'#''';;''''''''';''''''''''';;;''''''''';'''''''''''';;;;;;;''''++#+++++++'''+++++++++++
''''''''''''';;;;;;;;'';;;';;+'''++'''''''''''''''''''''';;'''''+'++++'++'';;'''''+++#########+++''''++++++++++++++++
'+++++''+++++++++++'+++'+#++++'+'''''''''''''''''''''';;;;;;;;;;;;;;;''';;''''''''''''''''''''++##+++++++++++++++++++
'''''';;'''''''''''''''+#''''''''''''''''''++++++';;''''''''''''''''''+###+######@#@@@@@#@@@@###++++''++'+'''++++++++
;'';;;;;;'''''''''''''##''''''''''';;;;;;;'''''+++++''''''''''''++####++####@@#@@##@####@@####+''+++''''''++++++''++#
'+++++++++++++'++++++#++++++++++'''''''''''''''';;'++++++++''''''''''+'#+######+##+++++#######+''''''''+++++''''+++++
'+++++++++++''''++''#++++++++'''''''''''''''''''''''''''''''''''''++#@##########@############+'+++++++'''''++++++++++
+++++++####+++++++++++''''''''''++'''''''''+++++++++++++'+++################################+'''''+++++++++++++++++++
++++++++++++++++++++++++++'''''''''''''''''++++++++++++++++++++++''+##################+++#+++++++++++++++++++++++++++
;''''''''''''''''''''''''''''''''''''''''''''++++''''''+++++'''''+###+####################++++++++++++++++++++++++++#
'++++'''''''''''''''+'+'+'''+++++''''''''''''''''''''++#############@@@@@###@@####@@@@@#++++++++++++++++''''++++#++++
+++++++++++++++++++++++++++++++++''''''''+####++++''+++++++########@@@@@#@@@@##@@@@@@#+++++++++++++++++++++++++++++##
++++++++++++++++++++++''''''''''''''''######################@@@@@@@@###@@@@##@@@@###++++++++++++++++++++#############
+++++######+++++++++++++++++++++++++##+''+''''+#@##########@#####@@#@@@@@@@@@@@@@#++++++++++++++++++++++++++##+++####
++++++++++++++++++++++++++++++++++++'++++''+'+++'++##########################++'+++++++++++'+++++++++++++++++++++++++
</pre><br><span style="padding-left: 27%;">Moonlapse Vertigo<span>"""
dat += """</body>"""


def overlord(request):
    return HttpResponse(dat)
