from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404, HttpResponse
from .models import Exam, Questions
from .forms import ExamForm, QuestionForm
from django.views.generic import CreateView, UpdateView, ListView, DetailView, View, TemplateView, DeleteView



def create_exam(request):
    if request.method == 'POST':
        exam_form = ExamForm(request.POST)
        if exam_form.is_valid():
            exam = exam_form.save()
            return redirect('App_Quiz:add_question', exam_id=exam.id)
    else:
        exam_form = ExamForm()

    return render(request, 'App_Quiz/create_exam.html', {'exam_form': exam_form})

def add_question(request, exam_id):
    exam = Exam.objects.get(pk=exam_id)

    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        if question_form.is_valid():
            question = question_form.save(commit=False)
            question.exam = exam
            question.save()
            return redirect('App_Quiz:add_question', exam_id=exam_id)
    else:
        question_form = QuestionForm()

    return render(request, 'App_Quiz/add_question.html', {'exam': exam, 'question_form': question_form})

def view_exam(request, exam_id):
    exam = Exam.objects.get(pk=exam_id)
    questions = Questions.objects.filter(exam=exam)
    return render(request, 'App_Quiz/view_exam.html', {'exam': exam, 'questions': questions})



class ExamList(ListView):
    context_object_name = 'exam_list'  # this 'blog' will be passed to html as dictionary
    model = Exam
    template_name = 'App_Quiz/exam_lists.html'


def take_exam(request, pk):
    exam = get_object_or_404(Exam, pk=pk)
    questions = Questions.objects.filter(exam=exam)
    

    if request.method == 'POST':
        correct_answers = 0
        total_ques_num=0
        
        for question in questions:
            total_ques_num += 1
            form = QuestionForm(request.POST, prefix=str(question.id))
            
          
            
            # retrieves the selected radio buttons value
            selected_option = request.POST.get(question.question)

            # Access the value of "op" for the current question
            selected_options_value = getattr(question, selected_option)
            
            #print(selected_options_value)
            # Check if the selected option is correct

            print(selected_option)
            if selected_options_value == question.ans:
                correct_answers += 1

            #print(question.ans)

        


        if total_ques_num == 0:
            return HttpResponse(    
                "<center><h1>No Question Added in this quiz<h1></center>"
            )
        else:
            score = (correct_answers / total_ques_num) *100
            return HttpResponse(
                
                "<center><h1>correct answers : "+ str(correct_answers)+" / "+ str(total_ques_num) +"<br>"
                "score : "+ str(score)+" %<h1></center>"
            )


    return render(request, 'App_Quiz/take_exam.html', {'exam': exam, 'questions': questions})
