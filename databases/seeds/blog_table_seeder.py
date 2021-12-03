"""BlogTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.Blog import Blog


class BlogTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        Blog.create({"title": "Vlogmas", "body":"Fun Activities"})
        Blog.create({"title": "Vlogmas2", "body":"Looking for sales!"})
        Blog.create({"title": "Vlogmas3", "body":"Enjoying family time"})
        pass
