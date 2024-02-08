from django.core.exceptions import ValidationError


class ContainsLetterValidator:
    def validate(self, password, user=None):
        if not any(char.isalpha() for char in password):
            raise ValidationError(
                'Le mot de passe doit contenir une lettre.', code='password_no_letters')
                
    def get_help_text(self):
        return 'Votre mot de passe doit contenir au moins une lettre majuscule ou minuscule.'
    
class ContainsDigitValidator:
    def validate(self, password, user=None):
        if not any(char.isdigit() for char in password):
            raise ValidationError(
                'Le mot de passe doit contenir un chiffre.', code='password_no_digit')
                
    def get_help_text(self):
        return 'Votre mot de passe doit contenir au moins un chiffre.'

    
class PostCodeValidator:
    def validate(self, password, user=None):
        if any(char.isalpha() for char in password):
            raise ValidationError(
                'Le mot de passe ne doit contenir aucune lettre.', code='cp_no_letters')
                
    def get_help_text(self):
        return 'Votre code postal doit avoir que des chiffres.'
    
