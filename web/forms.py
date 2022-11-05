from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, SetPasswordForm, PasswordChangeForm, PasswordResetForm
from django.contrib.auth.models import User
from base.models import Users as baseModel, Feedback, UserToken
'''
form that uses built in user creation form
'''
class UserForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True,
                                 widget=forms.TextInput(attrs={'class': 'form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none',
                                                                'placeholder': 'First Name'}))

    last_name = forms.CharField(max_length=50, required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none',
                                                                'placeholder': 'Last Name'}))

    username = forms.EmailField(max_length=50, required=True,
                                 widget=forms.TextInput(attrs={'class': 'form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none',
                                                                'placeholder': 'Email'}))
                                                               
    password1 = forms.CharField(max_length=50, required=True,
                                widget=forms.PasswordInput(attrs={'class': 'form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none',
                                                                'placeholder': 'Password'}))
    password2 = forms.CharField(max_length=50, required=True,
                                widget=forms.PasswordInput(attrs={'class': 'form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none',
                                                                'placeholder': 'Confirm Password'}))


    """
    Password validation is already validated by the UserCreationForm class in the built in form
    """
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(email=username).exists():
            raise forms.ValidationError("Email already exists")
        return username
    

'''
Basic model form that uses the Users model, extended from auth Model
'''
class UserProfileForm(forms.ModelForm):
    phone_number = forms.CharField(max_length=50, required=True,
                                      widget=forms.TextInput(attrs={'class': 'form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none',
                                                                'placeholder': 'Phone Number'}))
    class Meta:
        model = baseModel
        fields = ('phone_number',)

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if baseModel.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError("Phone number already exists")
        return phone_number


'''
Form that uses the model form to create a feedback form
'''
class ContactForm(forms.ModelForm):
    subject = forms.CharField(max_length=50, required=True,
                            
                                      widget=forms.TextInput(attrs={'class': 'form-control border text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-primary-500 focus:border-primary-500 shadow-sm-light',
                                                                'placeholder': 'Subject'}))
    email = forms.EmailField(max_length=50, required=True,
                                      widget=forms.TextInput(attrs={'class': 'form-control border text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-primary-500 focus:border-primary-500 shadow-sm-light',
                                                                'placeholder': 'Email'}))
    message = forms.CharField(max_length=500, required=True,
                                      widget=forms.Textarea(attrs={'class': 'form-control block p-2.5 w-full text-sm   rounded-lg shadow-sm border  focus:ring-primary-500 focus:border-primary-500 bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-primary-500 focus:border-primary-500',
                                                                'placeholder': 'Leave a message'}))
    class Meta:
        model = Feedback
        fields = ('subject', 'email', 'message')
    
    def clean_subject(self):
        name = self.cleaned_data['subject']
        return name
    
    def clean_message(self):
        message = self.cleaned_data['message']
        return message

'''
Form that uses the model form to create a Verification form
'''
class TwoStepForm(forms.ModelForm):
    two_step_code = forms.CharField(max_length=50, required=True,
                                      widget=forms.TextInput(attrs={'class': 'form-control border text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-primary-500 focus:border-primary-500 shadow-sm-light',
                                                                'placeholder': 'Enter code'}))
    class Meta:
        model = UserToken
        fields = ('two_step_code',)

    def clean_code(self):
        two_step_code = self.cleaned_data['two_step_code']
        return two_step_code


'''
Form that uses the built in form to create a login form
'''
class AuthForm(AuthenticationForm):
    username = forms.EmailField(max_length=50, required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none',
                                                                'placeholder': 'Username or Email'}))
    
    password = forms.CharField(max_length=50, required=True,
                                widget=forms.PasswordInput(attrs={'class': 'form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none',
                                                                'placeholder': 'Password'}))

    class Meta:
        model = User
        fields = ('username', 'password')

'''
Form that uses built in SetPasswordForm to create a password reset form
'''
class ForgottenPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(max_length=50, required=True,
                                widget=forms.PasswordInput(attrs={'class': 'form-control border text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-primary-500 focus:border-primary-500 shadow-sm-light',
                                                                'placeholder': 'New Password'}))
    
    new_password2 = forms.CharField(max_length=50, required=True,
                                widget=forms.PasswordInput(attrs={'class': 'form-control border text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-primary-500 focus:border-primary-500 shadow-sm-light',
                                                                'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ('new_password1', 'new_password2')


'''
Form that uses the built in PasswordResetForm to create a requesting password reset form
'''
class RequestPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(max_length=50, required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control border text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-primary-500 focus:border-primary-500 shadow-sm-light',
                                                                'placeholder': 'Username or Email'}))

    class Meta:
        model = User
        fields = ('email',)

'''
Form that uses the built in PasswordChangeForm to create a password change form
'''
class UpdatePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=50, required=True,
                                widget=forms.PasswordInput(attrs={'class': 'form-control border text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-primary-500 focus:border-primary-500 shadow-sm-light',
                                                                'placeholder': 'Old Password'}))
    
    new_password1 = forms.CharField(max_length=50, required=True,
                                widget=forms.PasswordInput(attrs={'class': 'form-control border text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-primary-500 focus:border-primary-500 shadow-sm-light',
                                                                'placeholder': 'New Password'}))
    
    new_password2 = forms.CharField(max_length=50, required=True,
                                widget=forms.PasswordInput(attrs={'class': 'form-control border text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-primary-500 focus:border-primary-500 shadow-sm-light',
                                                                'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')

