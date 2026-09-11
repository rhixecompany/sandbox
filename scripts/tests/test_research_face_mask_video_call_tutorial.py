"""Tests for scripts/research_face_mask_video_call_tutorial.py."""
import unittest

from research_test_common import make_research_tests

TestFaceMaskResearchScript = make_research_tests(
    script_name="research_face_mask_video_call_tutorial.py",
    topic_marker="face-mask-video-call-tutorial",
    sample_file="research/face-mask-video-call-tutorial/face-detection-on-video-stream-with-uv4l-raspberry-pi.md",
)

if __name__ == "__main__":
    unittest.main()