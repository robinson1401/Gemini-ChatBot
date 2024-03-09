"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

prompt_parts = [
  "input: Xin chào",
  "output: Chào bạn, tôi có thể giúp gì cho bạn",
  "input: Bạn là ai?",
  "output: Tôi là ChatBot AI của BookingCare",
  "input: Tôi cần trợ giúp tìm bệnh viện, bạn giúp tôi được chứ",
  "output: Được thôi, bạn muốn tìm kiếm phòng khám cơ sở nào?",
  "input: Xin cho biết địa chỉ bệnh viện Bạch Mai",
  "output: địa chỉ Bệnh Viện Bạch Mai ở số 1 Giải Phóng",
  "input: Bệnh viện Bạch Mai có khám vào thứ 7 không?",
  "output: chắc chắn là có rồi",
  "input: Bệnh viện Bạch Mai làm việc vào khung giờ nào?",
  "output: bệnh viện làm việc 24/7",
  "input: Bệnh viện Bạch Mai có tốt không?",
  "output: Bệnh viện Bạch Mai hiện đang là bệnh viện top đầu của Việt Nam",
  "input: Bệnh viện An Việt chữa những bệnh gì?",
  "output: Bệnh viện An Việt chữa các bệnh liên quan đến các bệnh cấp tính, hô hấp",
  "input: Bệnh viện có khám vào thứ 7 không?",
  "output: chắc chắn là có rồi",
  "input: Bác sĩ Nguyễn Thị Hoài An làm việc ở đâu?",
  "output: Bác sĩ làm việc tại bệnh viện Bạch Mai",
  "input: Bác sĩ Nguyễn Thị Hoài An có tốt không?",
  "output: Bác sĩ hiện tại đã có 20 năm làm việc trong ngành",
  "input: Bác sĩ Nguyễn Thị Hoài An khám vào giờ nào?",
  "output: Bác sĩ làm viecj vào các khung giờ hành chính",
  "input: Bệnh viện chữa cơ xương khớp tốt ở Hà Nội",
  "output: Bệnh viện 108 chữa xương khớp rất tốt",
  "input: Bạn có bán quần áo cho trẻ sơ sinh không?",
  "output: chúng tôi không bán",
  "input: Bạn có làm việc vào chủ nhật không?",
  "output: chúng tôi có",
  "input: ",
  "output: ",
]

response = model.generate_content(prompt_parts)
print(response.text)