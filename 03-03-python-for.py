WEEK_LIST = ['月', '火', '水', '木', '金', '土', '日']
SUBJECT_LIST = ['Python', '数学', '機械学習', '深層学習','エンジニアプロジェクト']


def output_schedule(study_time_list):
    '''今週の勉強予定を出力します'''
    study_subject_index = 0
    for week_str, study_volume in zip(WEEK_LIST, study_time_list):
        if study_volume == 0:
            print("{}曜日は、お休みです。".format(week_str))
        else:
            print("{0}曜日は{1}時間勉強する予定です。".format(week_str, study_volume))
            for limit in range(study_volume):
                study_subject_index += 1
                if study_subject_index == len(SUBJECT_LIST):
                    study_subject_index = 0
                print("{0}限目 {1}"
                .format(str(limit+1),SUBJECT_LIST[study_subject_index]))

def main():
    '''勉強情報をoutput_scheduleに渡します'''
    # 1日に何時間勉強するか（1週間　月曜日〜日曜日）
    study_time_list = [3, 1, 3, 0, 4, 2, 2]
    output_schedule(study_time_list)


if __name__ == '__main__':
    main()
