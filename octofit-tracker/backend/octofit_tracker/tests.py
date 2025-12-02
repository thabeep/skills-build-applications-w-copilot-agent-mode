from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create_user(username='testuser', email='test@example.com', team=self.team)
        self.activity = Activity.objects.create(user=self.user, type='run', duration=30)
        self.workout = Workout.objects.create(name='Test Workout', description='Test Desc')
        self.leaderboard = Leaderboard.objects.create(team=self.team, points=10)

    def test_user_team(self):
        self.assertEqual(self.user.team.name, 'Test Team')

    def test_activity_user(self):
        self.assertEqual(self.activity.user.username, 'testuser')

    def test_workout(self):
        self.assertEqual(self.workout.name, 'Test Workout')

    def test_leaderboard(self):
        self.assertEqual(self.leaderboard.team.name, 'Test Team')
        self.assertEqual(self.leaderboard.points, 10)
