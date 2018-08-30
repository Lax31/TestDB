import time
import yaml
from behave import *
from pywinauto import win32defines


@step('I Click index search')
def search_files(context):
    time.sleep(4)
    context.ftk_main.SetFocus()
#Click on index search tab
    context.ftk_main.right_click_input(coords=(521, 69))
    context.ftk_main.SetFocus()
    time.sleep(5)
    context.ftk_main.Maximize()
#Enter Search term
    context.ftk_main.click_input(coords=(31, 136))
    context.ftk_main.TypeKeys('thanks')
    time.sleep(4)
#Add & search
    context.ftk_main['Add'].Click()
    time.sleep(4)
    context.ftk_main['Search Now'].Click()
    time.sleep(1)
    context.ftk_main['Search Now'].double_click()
    context.ftk_main.click_input(coords=(1095, 224))
    time.sleep(2)
#Close indexed search filter popup dialog
    dlg_search_option = context.ftk_main['Indexed Search Filter Option']
    is_object_visible = dlg_search_option.IsVisible()
    print(is_object_visible)
    get_properties_for_popup = dlg_search_option.GetProperties()
    print(get_properties_for_popup)
    dlg_search_option.set_focus()
    key_focus = dlg_search_option.has_keyboard_focus()
    print(key_focus)
    time.sleep(4)
    #dlg_search_option.right_click_input(coords=(991, 577))
    act = dlg_search_option.VerifyActionable()
    print(act)
    dlg_search_option.Minimize()
    dlg_search_option.Restore()
    dlg_search_option.TypeKeys("{TAB 2}")
    # dlg_search_option.SendKeys('{ENTER}')
    # dlg_search_option['OK'].right_click()
    # dlg_search_option['OK'].ClickInput()

#Different options tried to no avail
    #dlg_search_option.TypeKeys("{ENTER}")
    #dlg_search_option.type_keys("{ENTER}")
    #dlg_search_option['OK'].ClickInput()

    #dlg_search_option(control_id=65525).TypeKeys("{ENTER}")

    '''dlg_active = dlg_search_option.wait('visible')
    dlg_active.right_click_input(coords=(991, 577))
    #print(dlg_active)
    state = dlg_active.get_show_state()
    print(state)
    bb = dlg_active.print_control_identifiers()
    print(bb)
    #dlg_active.move_window(coords=(225, 116))
    #dlg_active['Cancel'].ClickInput()
    a = dlg_active.debug_message()
    
    print(a)
    dlg_active.PrintControlIdentifiers()
    dlg_active(control_id=65525).TypeKeys("{ENTER}")
    #dlg_active.TypeKeys("{ENTER}")
    #btn = dlg_search_option.Button(1)
    #btn.Click()'''

    '''dlg_search_option.Properties.print_control_identifiers()
    dlg_search_option.Wait('ready', timeout=30, retry_interval=0.5)
    dlg_search_option = context.ftk_app['Indexed Search Filter Option']
    dlg_search_option.Wait('visible', timeout=20, retry_interval=0.5)
    dlg_search_option.set_focus()
    dlg_search_option.click_input(coords=(991, 577))
    #dlg_search_option['OK'].right_click()'''

    #dlg_search_option.SendKeys('{ENTER}')
    #context.ftk_main.SendKeys('{ENTER}')

    # context.ftk_main['Or'].Click()
    # context.ftk_main.Properties.print_control_identifiers()
    # context.ftk_main['Search Criteria:Edit'].type_keys("thanks")
    # context.ftk_main['Search CriteriaEdit'].type_keys("thanks")
    '''context.ftk_main['Search Criteria'].click_input()
    context.ftk_main['Search Criteria:Edit'].click_input()
    context.ftk_main['Search Criteria:edit'].type_keys("thanks")'''