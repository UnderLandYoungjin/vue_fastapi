<!-- 
📄 파일 경로: /project-root/frontend/src/App.vue

vue-i18n 언어 전환 테스트용 버튼을 추가한 App.vue 전체 코드.
영어, 한국어, 중국어 버튼을 클릭하면 문구가 실시간으로 바뀐다.
-->
<template>
  <div class="app">
    <!-- i18n 다국어 문구 -->
    <h1>{{ $t('message.hello') }}</h1>

    <!-- 언어 전환 버튼 -->
    <div class="buttons">
      <button @click="changeLanguage('en')">English</button>
      <button @click="changeLanguage('ko')">한국어</button>
      <button @click="changeLanguage('zh')">中文</button>
    </div>

    <!-- FastAPI에서 가져온 메시지 표시 -->
    <div class="api-section">
      <p>{{ apiMessage }}</p>
      <button @click="fetchApi">Fetch from FastAPI</button>
    </div>
  </div>
</template>

<script>
// Axios 인스턴스 불러오기
import api from './services/api'

export default {
  name: 'App',
  data() {
    return {
      apiMessage: ''  // FastAPI 응답 메시지 저장용
    }
  },
  methods: {
    // 언어 전환
    changeLanguage(lang) {
      this.$i18n.locale = lang
    },
    // FastAPI 호출
    async fetchApi() {
      try {
        const response = await api.get('/api/hello')
        this.apiMessage = response.data.message
      } catch (error) {
        console.error('API Error:', error)
        this.apiMessage = 'Failed to fetch from API'
      }
    }
  }
}
</script>

<style scoped>
.app {
  text-align: center;
  margin-top: 50px;
  font-family: Arial, sans-serif;
}

.buttons {
  margin-top: 20px;
}

button {
  margin: 0 10px;
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
}

.api-section {
  margin-top: 30px;
}
</style>
