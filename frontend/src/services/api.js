// api.js
// Axios 인스턴스를 생성하여 FastAPI 서버에 요청을 보낼 준비를 한다.
// baseURL은 FastAPI가 동작하는 서버 주소로 설정한다.

import axios from 'axios'

// Axios 인스턴스 생성 (여기서 baseURL은 FastAPI 백엔드 주소)
const api = axios.create({
  baseURL: 'http://221.152.105.81:8000',  // FastAPI 서버 주소
})

export default api  // 다른 Vue 컴포넌트에서 가져다 쓰도록 export
