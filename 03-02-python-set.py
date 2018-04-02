course_dict = {
    'AIコース': {'Aさん', 'Cさん', 'Dさん'},
    'Railsコース': {'Bさん', 'Cさん', 'Eさん'},
    'Railsチュートリアルコース': {'Gさん', 'Fさん', 'Eさん'},
    'JS': {'Aさん', 'Gさん', 'Hさん'},
}

# 関数のいい名前が思いつかない
def print_enrolled_person(want_to_find_person, check_course_name, check_course_member):
    # コースと受講生の積をとって、その数によって出力を帰る
    enroll_person = want_to_find_person & check_course_member
    enroll_person_count = len(enroll_person)
    if enroll_person_count == 0:
        print("{0}に{1}は在籍していません。"
            .format(check_course_name, want_to_find_person))
    if enroll_person_count == 1:
        print("{0}に{1}のみ在籍しています。"
            .format(check_course_name, enroll_person))
    if enroll_person_count > 1:
        print("{0}に{1}は在籍しています。"
            .format(check_course_name, enroll_person))


def find_person(want_to_find_person):
    """
    受講生がどのコースに在籍しているかを出力する。
    まずはフローチャートを書いて、どのようにアルゴリズムを解いていくか考えてみましょう。
    """
    # ここにコードを書いてみる
    for check_course_name, check_course_member in course_dict.items():
        print_enrolled_person(want_to_find_person, check_course_name, check_course_member)


def main():
    want_to_find_person = {'Cさん', 'Aさん'}
    print('探したい人: {}'.format(want_to_find_person))
    find_person(want_to_find_person)


if __name__ == '__main__':
    main()
