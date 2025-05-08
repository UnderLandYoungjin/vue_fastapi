// 📄 파일 경로: /project-root/frontend/src/i18n/index.js

// vue-i18n 기본 설정 파일이다.
// 여기에 다국어 메시지(예: 한국어, 영어, 중국어)를 등록한다.

import { createI18n } from 'vue-i18n'

const messages = {
  en: {
    message: {
      hello: 'Hello World!'
    }
  },
  ko: {
    message: {
      hello: '안녕하세요!'
    }
  },
  zh: {
    message: {
      hello: '你好！'
    }
  }
}

const i18n = createI18n({
  locale: 'en', // 기본 언어
  fallbackLocale: 'en',
  messages
})

export default i18n
