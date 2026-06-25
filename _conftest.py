import pytest


class TestBaseUrlFixtures:
    """测试 conftest.py 中的 base_url fixtures"""

    def test_base_url_1_returns_correct_url(self):
        """测试 base_url_1 fixture 返回正确的 URL"""
        expected_url = "https://jsonplaceholder.typicode.com"
        result = base_url_1()
        assert result == expected_url

    def test_base_url_1_returns_string_type(self):
        """测试 base_url_1 返回值类型为字符串"""
        result = base_url_1()
        assert isinstance(result, str)

    def test_base_url_1_returns_non_empty_string(self):
        """测试 base_url_1 返回非空字符串"""
        result = base_url_1()
        assert len(result) > 0

    def test_base_url_1_url_format_valid(self):
        """测试 base_url_1 URL 格式有效性"""
        result = base_url_1()
        assert result.startswith("https://")
        assert "jsonplaceholder" in result
        assert "typicode.com" in result

    def test_base_url_2_returns_correct_url(self):
        """测试 base_url_2 fixture 返回正确的 URL"""
        expected_url = "http://goappictest.sfjswl.com"
        result = base_url_2()
        assert result == expected_url

    def test_base_url_2_returns_string_type(self):
        """测试 base_url_2 返回值类型为字符串"""
        result = base_url_2()
        assert isinstance(result, str)

    def test_base_url_2_returns_non_empty_string(self):
        """测试 base_url_2 返回非空字符串"""
        result = base_url_2()
        assert len(result) > 0

    def test_base_url_2_url_format_valid(self):
        """测试 base_url_2 URL 格式有效性"""
        result = base_url_2()
        assert result.startswith("http://")
        assert "goappictest" in result
        assert "sfjswl.com" in result

    def test_base_url_1_and_base_url_2_are_different(self):
        """测试两个 fixture 返回不同的 URL"""
        url_1 = base_url_1()
        url_2 = base_url_2()
        assert url_1 != url_2

    def test_base_url_1_protocol_is_https(self):
        """测试 base_url_1 使用 HTTPS 协议"""
        result = base_url_1()
        assert "https://" in result
        assert "http://" not in result

    def test_base_url_2_protocol_is_http(self):
        """测试 base_url_2 使用 HTTP 协议"""
        result = base_url_2()
        assert "http://" in result
        assert "https://" not in result