# Allmytour-backend
- F.E<br>
  [김다슬](https://github.com/cocacollllla) :완벽완벽 다슬님<br>
  [황문실](https://github.com/LovelyMoon23) :열심열심 문실님<br>
  <br>
- B.E<br>
  [한상웅](https://github.com/tkddnd82) : 프로젝트 PM<br>
  [김훈태](https://github.com/kim-hoontae) : 연구연구 훈태님<br> 
  <br>

## 올마이투어000란?
- 올마이투어는 현재 코로나 이전에는 어딘가로 ‘떠나는 여행’이 주를 이루었다면, 코로나가 장기화되며  
  안전하게 ‘머무는 여행’이 라는 컨셉으로 스테이케이션 전문 플랫폼인 ‘올마이스테이’를 운영하고 있으며 
  코로나 이후 로컬 투어를 컨셉으로 하는 올마이투어0000 런칭을 준비하고 있으며 해당 프로젝트에 참여했습니다.
- 개발은 초기 세팅부터 직접 구현했으며, 프론트와 백을 연결해 실제 사용 가능한 수준으로 개발했습니다.

### 개발 인원 및 기간

- 개발기간 : 2021/9/01 ~ 2021/9/28
- 개발 인원 : 프론트엔드 2명, 백엔드 2명

### 적용 기술

> -Front-End : javascript, React.js framwork, sass<br>
> -Back-End : Python, Django web framework, MySQL, Bcrypt, pyjwt, Maria DB , Centos7<br>
> -Common : POSTMAN, RESTful API

### 구현 기능

#### 회원가입 / 로그인페이지
- bcrypt 암호화 
- JWT Access Token 전송
- 유효성 검사 (중복, 정규식)
- 자동 로그인 (로그인 상태 유지기능)
- Refresh Token(Access Token만료시)을 통한 보안성 강화
- 구글 API활용한 이메일 인증 : 
   비밀번호 찾기에서 이메일을 통해서 인증링크를 전송해서 해당 링크를 통해 유저의 유효성을      
   검사하며 링크의 만료시간전에 비밀번호 수정을 마무리 하도록 구현
- 네이버 API활용한 SMS 인증:
   핸드폰을 통해 인증코드 발송해 해당 인증코드 입력을 통해서 인증할수 있도록 구현.
- 비밀번호 찾기 및 재 설정
- 서버 구축 및 데이터 베이스(Maria DB) 구축: 서버와 데이터 베이스 일원화 구현.

#### 리팩토링 진행
- 회원가입 / 로그인을 소셜 로그인(카카오) 통해 구현
  카카오 API 통한 access token을 통해 유저 정보 획득 뒤 다시 새로운 access_token 부여하여 유저 관리

#### 데이터 입력 및 배포
- RDS DB 통해 멤버 데이터베이스 일원화
- csv 파일 제작 후 api 구성하여 데이터 한 번에 입력
- AWS 배포 통한 데이터베이스 배포 완료
<br>

## Reference
- 실무수준의 프로젝트이지만 학습용으로 만들었기 때문에 이 코드를 활용하여 이득을 취하거나 무단 배포할 경우 법적으로 문제될 수 있습니다.
