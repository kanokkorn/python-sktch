import pyautogui as pg

spotify_icon = pg.locateCenterOnScreen("./pyautogui/image/spotify.png", confidence=0.9)
pg.click(spotify_icon)
search_bar = pg.locateCenterOnScreen("./pyautogui/image/search_bar.png", confidence=0.9)
pg.click(search_bar)
pg.typewrite("narrative", interval=0.2)
pg.hotkey("enter")
narrative = pg.locateCenterOnScreen("./pyautogui/image/narrative.png", confidence=0.9)
pg.click(narrative)

