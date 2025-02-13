from django.test import TestCase
from downloader.views import download_video_view

# Create your tests here.
class DownloadVideoViewTest(TestCase):
    def test_download_video_view_status_code(self):
        response = self.client.get('/download - video - url/')  # 假设这是下载视频视图对应的URL
        self.assertEqual(response.status_code, 200)

from downloader.models import DouyinVideo

class DouyinVideoModelTest(TestCase):
    def test_create_douyin_video(self):
        video = DouyinVideo(video_url='https://example.com/douyin - video', is_downloaded=False)
        video.save()
        self.assertEqual(DouyinVideo.objects.count(), 1)        

from downloader.views import parse_douyin_video_url  # 假设存在此解析函数

class VideoUrlParseTest(TestCase):
    def test_parse_douyin_video_url(self):
        result = parse_douyin_video_url('https://www.douyin.com/video/12345')
        self.assertEqual(isinstance(result, str), True)  # 假设解析结果为字符串类型