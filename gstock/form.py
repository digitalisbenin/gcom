
from django import forms
from django.forms import formset_factory, inlineformset_factory
from contact.models import Contact
from gstock.models import CommandeClient, CommandeFournisseur, FamilleProduit, GroupeTaxe, LigneCommande, LigneCommandeClient, Produit, UniteMesure




class FamilleForm(forms.ModelForm):
    class Meta:
        model = FamilleProduit
        fields = '__all__'
        widgets = {
            'libele': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Libellé' }),
            'description': forms.Textarea(attrs={'class': 'form-control','rows':3, 'placeholder': 'Description'}),
            }



class UniteMesureForm(forms.ModelForm):
    class Meta:
        model = UniteMesure
        fields = '__all__'
        widgets = {
            'libele': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Libellé'}),
            'description': forms.Textarea(attrs={'class': 'form-control','rows':3, 'placeholder': 'Description'}),
            }


class GroupeTaxeForm(forms.ModelForm):
    class Meta:
        model = GroupeTaxe
        fields = '__all__'
        widgets = {
            'libele': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Libellé'}),
            'taux': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'code_fiscal': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Code fiscal'}),
            'exoneration': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'statut': forms.Select(attrs={'class': 'form-control'}),
        }




class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = '__all__'
        widgets = {
            'libele': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Libellé'}),
            'code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Code'}),
            'description': forms.Textarea(attrs={'class': 'form-control','rows':3, 'placeholder': 'Description'}),
            'cout_achat': forms.NumberInput(attrs={'class': 'form-control','min': '0', 'placeholder': 'Coût d\'Achat'}),
            'prix': forms.NumberInput(attrs={'class': 'form-control', 'min': '0','placeholder': 'prix de vente'}),
            'quantite': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantité en Stock'}),
            'famille': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Famille'}),
            'fournisseur': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Fournisseur'}),
            'unite_mesure': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Unité de Mesure'}),
            'groupe_taxe': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Groupe de Taxes'}),
            'date_peremption': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'Date de Péremption'}),
            'niveau_alerte_stock': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Niveau d\'Alerte de Stock'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Image du Produit'}),
        }






# class CommandeFournisseurForm(forms.ModelForm):
#    class Meta:
#         model = CommandeFournisseur
#         fields = ['fournisseur', 'date_commande', 'produits', 'statut', 'reference', 'date_reception']
#         widgets = {
#             'date_commande': forms.DateInput(attrs={'type': 'date'}),
#             'date_reception': forms.DateInput(attrs={'type': 'date'}),
#             'reference': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Réference'}),
#             'statut': forms.Select(attrs={'class': 'form-control'}),
#             'fournisseur': forms.Select(attrs={'class': 'select2'}),
#             'produits': forms.SelectMultiple(attrs={'class': 'select2'}),
#         }

class CommandeFournisseurForm(forms.ModelForm):
    
    class Meta:
        model = CommandeFournisseur
        # fields = '__all__'
        fields = ['fournisseur', 'date_commande', 'reference']
        widgets = {
            'fournisseur': forms.Select(attrs={'class': 'select2 form-control','label':''}),
            'date_commande': forms.DateInput(attrs={'type': 'date', 'class': 'form-control','label':''}),
            'reference': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Réference','label':''}),
            
        }
        

class LigneCommandeForm(forms.ModelForm):
    class Meta:
        model = LigneCommande
        fields = ['commande','produit', 'quantite', 'prix_unitaire', 'montant']
        widgets = {
            'produit': forms.Select(attrs={'class': 'select2 form-control'}),
            'quantite': forms.NumberInput(attrs={'class': 'form-control'}),
            'prix_unitaire': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'montant': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }
        
        
class CommandeClientForm(forms.ModelForm):
    class Meta:
        model = CommandeClient
        # fields = '__all__'
        fields = ['client', 'date_commande', 'reference']
        widgets = {
            'client': forms.Select(attrs={'class': 'select2 form-control','label':''}),
            'date_commande': forms.DateInput(attrs={'type': 'date', 'class': 'form-control','label':''}),
            'reference': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Réference','label':''}),
            
        }

class LigneCommandeClientForm(forms.ModelForm):
    class Meta:
        model = LigneCommandeClient
        fields = ['commande_client','produit', 'quantite', 'prix_vente', 'montant']
        widgets = {
            'produit': forms.Select(attrs={'class': 'select2 form-control'}),
            'quantite': forms.NumberInput(attrs={'class': 'form-control'}),
            'prix_vente': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'readonly': 'readonly'}),
            'montant': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'readonly': 'readonly'}),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Définissez la valeur par défaut pour le champ produit_id ici
        self.fields['produit'].initial = Produit.objects.get(pk=1)
        
        
        
        
        
LigneCommandeFormSet = inlineformset_factory(CommandeFournisseur, LigneCommande, form =LigneCommandeForm,extra=1, can_delete=True, can_delete_extra=True)
LigneCommandeClientFormSet = inlineformset_factory(CommandeClient, LigneCommandeClient, form =LigneCommandeClientForm,extra=1, can_delete=True, can_delete_extra=True)
