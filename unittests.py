import base64
import unittest

import main
import model_handler


class ControllerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = main.app
        self.app.config["TESTING"] = True
        self.client = self.app.test_client(self)
        with open(r"C:\Users\Dkrd\Documents\GitHub\ocr_deployment_test_task\test.jpg", "rb") as img:
            self.test_image = base64.b64encode(img.read())

        self.payload = {"img": self.test_image}

    def test_predict(self):
        result = main.mh.predict(self.payload["img"])

        self.assertIs(type(result), list)

    def test_predict_invalid(self):
        result = main.mh.predict("mock data")

        self.assertIs(type(result), list)
        self.assertEqual(len(result), 0)

    def test_predict_post(self):
        response = self.client.post("/text-recognition", data=self.payload)

        self.assertEqual(response.status_code, 200)
        self.assertIs(type(response.json), list)

    def test_predict_post_invalid(self):
        response = self.client.post("/text-recognition", data="mock_data")

        self.assertEqual(response.status_code, 400)


if __name__ == "__main__":
    unittest.main()
