from task2 import file_name, report

# +4 điểm cho mỗi câu trả lời đúng
# 0 điểm cho mỗi câu trả lời bị bỏ qua
# -1 điểm cho mỗi câu trả lời sai
answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"

try:
    df = report(file_name)
    #get result valid
    result_valid_df = df[df["type"] == "valid" ]
    #list answer key
    answer_key = answer_key.split(",")
    list_scores = []
    #total student have score > 80
    gt_80 = 0
    #list index answer false
    lst_ans_false=[]
    #list answer pass
    lst_ans_pass=[] 
    for idx, row in result_valid_df.iterrows():
        answer = row["answer"]
        compare = zip(answer_key, answer)
        score=0

        for idx_, com in enumerate(compare):
            #com[0]: answer true, com[1]: answer of student
            if com[0] == com[1]:
                score+=4
            elif com[1] == '':
                score+=0
                lst_ans_pass.append(idx_)
            else:
                score-=1
        
        if score > 80:
            gt_80+=1
        list_scores.append(score)

        #get list answer false
        for _idx, value in enumerate(answer):
            if value == '':
                lst_ans_false.append(_idx + 1)

    #score>80
    print("total students have score > 80: ", gt_80)
    #avg score
    avg_score = sum(i for i in list_scores) / len(list_scores)
    print("average score: ", "{:.2f}".format(avg_score))
    #max score
    print("max score: ", max(list_scores))
    #min score
    print("min score: ", min(list_scores))
    #value domain
    print("value domain of score: ", max(list_scores)-min(list_scores))
    #median
    import statistics
    print("median: ", statistics.median(list_scores))
    #answer false
    import collections
    _counter_false = collections.Counter(lst_ans_false).most_common()
    ans_false = [ i[0] for i in _counter_false if i[1] == _counter_false[0][1]]
    print("answer incorrectly most: ", ans_false)
    #answer pass
    _counter_pass = collections.Counter(lst_ans_pass).most_common()
    ans_pass = [ i[0] for i in _counter_pass if i[1] == _counter_pass[0][1]]
    print("answer skip most: ", ans_pass)
except Exception:
    print("Sorry, I can't find this filename")
    

