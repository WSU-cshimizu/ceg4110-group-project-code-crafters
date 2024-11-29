from django.test import TestCase
from django.urls import reverse
from userAccounts.models import *
from mainApp.models import *

class CLABallotTest(TestCase):

    def setUp(self):
        self.user = Account.objects.create(email='testuser@example.com', department='CLA', verified=True)
        self.user.save()
        self.client.force_login(self.user)
        self.candidate1 = CLA_Candidate.objects.create(fullname='Candidate 1', position='President')
        self.candidate2 = CLA_Candidate.objects.create(fullname='Candidate 2', position='Vice President')

    def test_prevent_duplicate_votes(self):
        data = {

            'president': self.candidate1.id,
            'vicepresident': self.candidate2.id,
        }
        
        self.client.post(reverse('CLAballot'), data)
        
        UserRecords.objects.create(
        owner=self.user,
        department='CLA',
        president=self.candidate1.fullname,
        vice_president=self.candidate2.fullname,
        )

        self.user.voted_department = True
        self.user.save()

        # Attempt to vote again
        response = self.client.post(reverse('CLAballot'), data)
        self.assertRedirects(response, reverse('Records'), status_code=302)