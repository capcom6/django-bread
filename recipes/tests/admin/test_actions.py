from django.contrib.admin.sites import AdminSite
from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from unittest.mock import Mock


from recipes.admin.admin import CommentAdmin
from recipes.models import Comment


class CommentsAdminTest(TestCase):
    fixtures = ["categories.json", "programs.json", "recipes.json", "comments.json"]

    def setUp(self):
        self.client = Client()
        self.site = AdminSite()
        self.user = get_user_model().objects.create_user(
            username="testuser", password="testpass", is_staff=True, is_superuser=True
        )
        self.client.login(username="testuser", password="testpass")
        self.model_admin = CommentAdmin(model=Comment, admin_site=self.site)

    def test_action_accept(self):
        request = Mock(user=self.user, GET={})
        actions = self.model_admin.get_actions(request)

        expected_results = [
            ("comment_accept", Comment.STATE_ACCEPTED),
            ("comment_reject", Comment.STATE_REJECTED),
        ]
        queryset = Comment.objects.all()
        comments_count = queryset.count()

        for action_name, state in expected_results:
            action_meta = actions.get(action_name)
            self.assertIsNotNone(action_meta)

            action = action_meta[0]

            action(self.model_admin, request, queryset)

            self.assertEqual(queryset.filter(state=state).count(), comments_count)
