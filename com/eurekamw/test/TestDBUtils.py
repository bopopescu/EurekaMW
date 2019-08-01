from com.eurekamw.model import WordFile as wf, UserFile as uf
from com.eurekamw.utils import DBUtils as dbu


def test_insert_word():
    test_word  = wf.Word('testword', 'testcategory', 'test stems', 'test shortdef', 'test xdef')
    result = dbu.insert_word(test_word)
    if result is True:
        print("Word inserted in the db successfully")
    else:
        print("Problem in inserting the word")


def test_is_username_unique():
    test_username = 'administrator'
    result = dbu.is_username_unique(test_username)
    if result is True:
        print("Username is available")
    else:
        print("Username is not available")


def test_add_user():
    test_user = uf.User('administrator','Admin', 'password')
    dbu.add_user(test_user)

def main_test_suite():
    #test_insert_word()
    #test_is_username_unique()
    test_add_user()

main_test_suite()