# 약속은 아님
from django import forms
from .models import Article

# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)
#     # 인풋의 표현방식 변경은 이제 forms.py에서 진행하기. not템플릿

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class':'my-title',
                'placeholder':'Enter the title',
            }
        ),
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class':'my-content',
                'placeholder':'Enter the content',
                'rows':5,
                'cols':50,
            }
        ),
        error_messages={'required':'내용을 입력해주세요.'},
    )
    class Meta:
        model = Article     # 필수로 지정
        fields = '__all__'  #  출력할 것(fields) 아닐 것(exclude, =[]or('title')) 지정
        # 전체필드는 '__all__'

        # 모델파일을 분석해서 폼을 만들어줌
