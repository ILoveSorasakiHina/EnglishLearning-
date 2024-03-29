import csv, io, random,openai
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from .models import Word,user
from .forms import LoginForm,RegisterForm,WordFrom


# 註冊
def sign_up(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')  #重新導向到登入畫面
    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def sign_in(request):
    form = LoginForm()
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')  #重新導向到首頁
    context = {
        'form': form
    }
    return render(request, 'login.html', context)

# def remember_word(request):
#     form = WordFrom
#     if request.method == "POST":
#         word = request.POST.get("word")
#         user.objects.update_or_create(get_all_word)
#         return HttpResponse("輸入成功")
#     return render(request,'')
        

#讀入html並輸出
def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

#禁用csrf保護，不然無法完成功能
@csrf_exempt
def upload_csv(request):
    #以UTF-8編碼讀取文件，並跳過第一行
    if request.method == 'POST':
        csv_file = request.FILES['file']
        data_set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        next(io_string)
        #分割元素並寫入資料庫，有相同word則更新，無則創建新資料
        for column in csv.reader(io_string, delimiter=',', quotechar="|"):
            created =  Word.objects.update_or_create(
                word=column[0],
                part_of_speech=column[1],
                meaning=column[2],
                #依難度調整level的數字
                level = 6
            )
        return HttpResponse("CSV文件已成功上傳並保存到資料庫中！")
    else:
        return render(request,"upload_csv.html")
    
# def delete_same_word(self):



def delete_all_word():
    #刪庫走人
    words=Word.objects.all()
    words.delete()
    return HttpResponse("刪除成功!")
    
def get_all_word(request,key):
    #讀取單字
    try:
        words = Word.objects.filter(level=key)
        return render(request,"words.html",{"words" : words,"key":key})
    except Exception as e:
        print(e)
        

def quiz(request):
    # 從資料庫中獲取所有單詞
    words = Word.objects.all()

    # 隨機選擇一個單詞作為問題
    question_word = random.choice(words)

    # 隨機選擇三個單詞作為錯誤答案
    wrong_words = random.sample([word for word in words if word != question_word], 3)

    # 將所有答案混合並隨機排序
    all_words = [question_word] + wrong_words
    random.shuffle(all_words)

    # 將正確答案儲存到 session 中
    request.session['correct_answer'] = question_word.word

    return render(request, 'quiz.html', {
        'question': question_word.meaning,
        'choices': [(word.word, word == question_word) for word in all_words]
    })

# def quiz2(request):
#     words = Word.objects.all()
#     question_word = random.sample([word for word in words],4)

#     openai.api_key = ''

#     completion = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "teacher", "content": f"{question_word} 請就這四個單字出一個克漏字選擇題"}
#     ]
# )
    


def submit_answer(request):
    if request.method == 'POST':
        # 從 POST 請求中獲取答案
        answer = request.POST.get('answer')

        # 從 session 中獲取正確答案
        correct_answer = request.session.get('correct_answer')

        # 檢查答案是否正確
        is_correct = (answer == correct_answer)

        # 將結果儲存到 session 中
        request.session['is_correct'] = is_correct

        # 重定向到結果頁面
        return redirect('result')

    # 如果不是 POST 請求，則重定向到測驗頁面
    return redirect('quiz')

def result(request):
    # 從 session 中獲取答案
    is_correct = request.session.get('is_correct')

    # 渲染結果頁面
    return render(request, 'result.html', {
        'is_correct': is_correct,
    })



    


