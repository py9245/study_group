'''
## 1. 자바스크립트 기초 문법
### 1-1. 변수 & 선언 키워드
**1) 변수 이름 규칙 / 컨벤션**

- 시작: 문자, `$`, `_` 로 시작
- 대소문자 구분, 예약어(`for`, `if`, `function` …) 사용 X
- 네이밍 컨벤션
  - `camelCase` : 변수, 함수, 객체
  - `PascalCase` : 클래스, 생성자
  - `SNAKE_CASE` : 변경되지 않는 상수

**호이스팅**
- 변수와 함수 선언이 해당 스코프의 최상단으로 끌어올려진 것처럼 동작하는 현상
- var 호이스팅 : 선언과 동시에 undefined
- let과const 호이스팅 : 호이스팅은 되지만, 초기화 되지 않음 , 선언문 이전에 변수에 접근하면 ReferenceError 발생, 이 구간을 TDZ(Temporal Dead Zone, 일시적 사각지대)라고 함

**2) var / let / const 차이**

- `var`
  - 함수 스코프
  - 중복 선언 O, 재할당 O
  - 호이스팅 시 `undefined` 로 초기화
- `let`
  - 블록 스코프
  - 중복 선언 X, 재할당 O
  - 호이스팅 되지만 **TDZ(Temporal Dead Zone)** 때문에 선언 전 사용 불가
- `const`
  - 블록 스코프
  - 중복 선언 X, 재할당 X
  - **참조값(주소)** 를 못 바꾸는 것뿐, 객체/배열 안의 내용은 변경 가능

**시험 포인트**
- “`var`, `let`, `const` 차이 설명하시오”
- “재할당 필요 없으면 왜 `const`를 기본으로 쓰는가?”  
  → 의도 명확 + 버그 예방

---

### 1-2. 데이터 타입

**1) 원시 자료형 vs 참조 자료형**

- 원시(Primitive): `Number`, `String`, `Boolean`, `null`, `undefined`
  - 값 자체 저장, 불변(immutable)
  - 변수에 다른 변수 대입 시 **값 복사**
- 참조(Reference): `Object`, `Array`, `Function` 등
  - **주소(참조값)** 저장, 가변(mutable)
  - 다른 변수에 대입 시 **주소 복사 → 같은 객체를 가리킴**

**2) Template Literal**

- 백틱 `` ` `` 사용
- `\n` 없이 여러 줄 문자열 가능
- 변수/표현식 삽입: `` `Hello, ${name}!` ``

**3) NaN / null / undefined**

- `NaN` : 숫자 연산 실패 시 (예: `Number('abc')`)
- `null` : “의도적으로 값이 없음”
- `undefined` : “값을 아직 안 넣었거나, 존재하지 않는 프로퍼티”

**시험 포인트**
- “원시 타입과 참조 타입 차이 설명”
- `==` 비교에서 `null` vs `undefined` 어떻게 동작하는지  
  (둘은 느슨한 동등 연산에서 같다고 취급)

---

### 1-3. 연산자 / 조건문 / 반복문

**1) 주요 연산자**

- 할당 연산자: `=`, `+=`, `-=`, `*=`, …
- 증가/감소: `++a` / `a++` (반환 값 타이밍)
- 비교 연산자: `<`, `>`, `<=`, `>=`
- 동등 / 일치:
  - `==` : 타입 자동 변환 후 값만 비교
  - `===` : 타입, 값 모두 비교 (시험에서 **권장**하는 연산자)
- 논리 연산자: `&&`, `||`, `!`  
  → **단축 평가**(앞에서 이미 결과 확정되면 뒤를 안 보는 것)

**2) 조건문**

- `if / else if / else`
- `switch` : 하나의 변수에 여러 케이스 분기
- 삼항 연산자: `조건 ? 값1 : 값2`

**3) 반복문**

- `while (조건) { ... }`
- `for (초기값; 조건; 증감) { ... }`
- `for...in`
  - “**키**(index, property name)” 를 순회
  - **객체** 반복용, 배열엔 잘 안 씀(순서 보장 X)
- `for...of`
  - “값(value)” 를 순회
  - 배열, 문자열 등 **iterable** 에 사용

**시험 포인트**
- “배열은 `for...of`를 권장하는 이유?”
- “`for...in`과 `for...of` 차이”

---

### 1-4. 함수 / 화살표 함수 / 매개변수

**1) 함수 선언식 vs 함수 표현식**

- 선언식

  ```js
  function add(a, b) { 
    return a + b
  }
  ```

  - **호이스팅 O** (선언 전에도 사용 가능)

- 표현식

  ```js
  const add = function (a, b) { 
    return a + b 
  }
  ```

  - **호이스팅 X** (선언 이후에만 사용 가능)
  - 요즘은 대부분 “표현식 + const” 패턴 많이 사용

**2) 매개변수**

- 기본값 매개변수

  ```js
  function greet(name = 'Guest') {
    console.log(`Hello, ${name}`)
  }
  ```

- 나머지 매개변수(Rest)

  ```js
  function sum(...nums) {
    return nums.reduce((acc, cur) => acc + cur, 0)
  }
  ```

  - 나머지 매개변수는 **하나만**, 항상 **마지막 위치**에만 가능

- 매개변수 & 인자 개수 불일치
  - 매개변수 > 인자 → **없는 인자는 `undefined`**
  - 매개변수 < 인자 → **초과 인자는 무시**

**3) 전개 구문(Spread syntax)**

- **배열/객체 펼치기**

  ```js
  const arr2 = [...arr1, 10, 20]
  func(...arr)  // 배열을 각각의 인자로 전달

  const obj3 = { ...obj1, ...obj2 }
  ```

**4) 화살표 함수**

```js
const add = (a, b) => a + b
```

- `function` 키워드 대신 `=>`
- 한 줄짜리 표현식이면 `{}`와 `return` 생략 가능
- `this` 바인딩 방식이 다름 (보통 “상위 스코프의 this를 유지”)

**시험 포인트**
- “선언식/표현식/화살표 함수 차이”
- “나머지 매개변수 문법 제약”
- “전개 구문(spread)과 나머지 매개변수(rest)의 쓰임 차이”

---

## 2. 객체 / 배열 / JSON / 콜백 / 클래스

### 2-1. 객체(Object)

**1) 객체 구조**

```js
const user = {
  name: 'Tom',
  age: 20,
  sayHi() {
    console.log('Hi')
  },
}
```

- 속성 참조
  - 점 표기: `user.name`
  - 대괄호: `user['name']` (동적 키, 공백 포함 키 등)
- `'key' in obj` 연산자 → 속성 존재 여부 확인

**2) 메서드(Method)**

- 객체 안에 정의된 함수
- `this` : 메서드가 속한 객체 자체를 가리킴

---

### 2-2. JSON & 배열

**1) JSON**

- JavaScript Object 표기법 기반의 **문자열 포맷**
- 변환
  - 객체 → JSON 문자열 : `JSON.stringify(obj)`
  - JSON 문자열 → 객체 : `JSON.parse(jsonStr)`

**2) 배열 기본 메서드**

- `push`, `pop`, `shift`, `unshift`
- `indexOf`, `includes`, `slice`, `splice` 등

**3) Array Helper Methods**

- `forEach` : 각 요소에 대해 콜백 실행, **반환 값 없음**
- `map` : 콜백 결과로 **새 배열 반환**
- `filter` : 콜백에서 `true`인 요소만 모은 **새 배열**
- `find` : 조건을 만족하는 **첫 번째 요소** 반환 (못 찾으면 `undefined`)
- `some` : 하나라도 조건 만족 → `true`, 없으면 `false`
- `every` : 모두 조건 만족해야 `true`
- `reduce` : 누적값을 만들어낼 때 사용

**4) forEach에서 break 불가**

- `forEach`는 중간에 `break`로 끊을 수 없음
- 대신
  - `some` : 원하는 순간 `true` 반환 → 사실상 break처럼 사용
  - `every` : 원하는 순간 `false` 반환 → 마찬가지

**시험 포인트**
- “`map`과 `forEach` 차이 (반환 유무)”
- “`find`와 `filter` 차이”
- “forEach에서 break 안 되는 이유, 대안”

---


### 2-3. 콜백 함수

- 정의: **다른 함수에 인자로 전달되는 함수**

```js
function repeat(n, callback) {
  for (let i = 0; i < n; i++) {
    callback(i)
  }
}

repeat(3, (i) => console.log(i))
// 0
// 1
// 2
```

- 장점
  - 함수 유연성 : 같은 함수(`map`)도 어떤 콜백을 주냐에 따라 동작 달라짐
  - 비동기 처리 : `setTimeout`, `addEventListener` 등에서 콜백 사용

**시험 포인트**
- “콜백 함수란 무엇인가, 예시와 함께 설명”
- **함수 이름만 넘기는 것**과 `func()` 처럼 호출 결과를 넘기는 것 차이

---

### 2-4. 클래스(Class)

- ES6의 `class` 문법

```js
class Person {
  constructor(name) {
    this.name = name
  }

  sayHi() {
    console.log(`Hi, ${this.name}`)
  }
}

const p = new Person('Tom')  // 인스턴스 생성
p.sayHi()
```

- `constructor` : 인스턴스 생성 시 자동으로 호출
- 메서드는 `.prototype`에 저장 (클래스는 기존 프로토타입 기반 상속의 문법 설탕)

**시험 포인트**
- “class/constructor/new의 관계”
- “클래스 인스턴스와 일반 객체의 개념적 차이”

---

## 3. DOM & 이벤트

### 3-1. DOM 기본

- DOM(Document Object Model)
  - HTML 문서를 **트리 구조 객체**로 표현한 것
  - JS가 HTML/CSS를 조작할 수 있게 해주는 구조

- `document` 객체
  - DOM 트리의 최상단 진입점
  - 페이지의 모든 요소/텍스트/속성에 접근 가능

**요소 선택 메서드(대표)**

- `document.getElementById('id')`
- `document.querySelector('css selector')`
- `document.querySelectorAll('css selector')`

**속성/내용 조작**

- `element.textContent` : 텍스트 내용 (태그 해석 X)
- `element.innerHTML` : HTML을 문자열로 삽입/읽기 (XSS 위험 주의)
- `element.classList.add / remove / toggle`
- `element.setAttribute / getAttribute / removeAttribute`

**DOM 구조 조작**

- `document.createElement(tagName)`
- `parent.appendChild(child)`
- `parent.removeChild(child)`

---

### 3-2. Event 기본

**1) 이벤트란**

- 웹 페이지에서 발생하는 **모든 사건**  
  (click, input, submit, scroll …)

**2) 이벤트 리스너 등록**

```js
element.addEventListener('click', (event) => {
  // ...
})
```

- `event` 객체
  - `event.type` : 이벤트 종류
  - `event.target` : 실제 이벤트가 발생한 요소
  - `event.currentTarget` : 핸들러가 등록된 요소
  - 키보드 이벤트: `event.key`, `event.code` 등

**3) 자주 쓰는 이벤트 종류**

- Mouse : `click`, `dblclick`, `mouseover`, `mouseout`, …
- Form/Input : `input`, `change`, `submit`
- Keyboard : `keydown`, `keyup`
- 기타 : `scroll`, drag & drop 이벤트 등

**4) 기본 동작 막기**

- `event.preventDefault()`  
  (예: form submit 시 페이지 새로고침 막기, `<a>` 링크 이동 막기)

---

### 3-3. 이벤트 버블링 / 캡처링 / 위임

**1) 이벤트 흐름 단계**

1. **캡처링 단계** : 상위(최상위 조상) → 타겟으로 내려감
2. **타겟 단계** : 실제 요소에서 핸들러 동작
3. **버블링 단계** : 타겟 → 상위 조상으로 올라감

**2) 버블링**

- 어떤 요소에서 이벤트가 발생하면,
  - 그 요소의 핸들러 실행 후
  - 부모 → 조상 순으로 핸들러가 계속 실행되는 것

**3) 왜 필요한가? (이벤트 위임)**

- 비슷한 버튼이 여러 개일 때, 각각에 핸들러 X
- 공통 부모에 핸들러 하나만 달고, `event.target`으로  
  **어떤 버튼인지 판별**
- → 동적 요소가 많을 때 성능/관리 상 유리

**4) event.target vs event.currentTarget**

- `target` : 실제 클릭된 **최하위 요소**
- `currentTarget` : 지금 실행 중인 핸들러가 달린 **요소**

**5) 기본 동작 취소 & 전파 제어**

- `event.preventDefault()` : 기본 동작 막기 (form submit, 링크 이동 등)
- `event.stopPropagation()` : 이벤트 상위로 전파(버블링) 막기

---

### 3-4. input / keyup / scroll / drag

**1) Input Event**

- 입력 필드 내용이 **바뀔 때마다** 발생
- 타이핑, 붙여넣기 등
- 실시간 유효성 검사에 많이 사용

**2) Keyup Event**

- 키보드를 눌렀다가 **뗄 때** 발생
- Enter를 눌렀을 때만 제출 같은 처리 가능

**3) Scroll Event**

- 스크롤할 때 발생
- 예: 상단 고정 내비게이션, “위로 가기” 버튼 표시 등

**4) Drag & Drop 관련 이벤트**

- 드래그되는 요소에서:
  - `dragstart`, `drag`, `dragend`
- 드랍 영역에서:
  - `dragenter`, `dragover`, `dragleave`, `drop`

- **중요 포인트**
  - `dragover`에서 `event.preventDefault()` 해줘야  
    `drop` 이벤트가 정상 동작

---

### 3-5. 세미콜론(;) & ASI

- JS에서 세미콜론은 **선택적**
- JS 엔진이 자동으로 `ASI(Automatic Semicolon Insertion)` 수행
- 하지만 줄바꿈 위치에 따라 의도치 않은 ASI가 일어나 버그 될 수 있어서
  - 보통 **명시적으로 세미콜론 쓰는 스타일**이 안전

---

## 4. 한 번에 정리하는 “시험 핵심 암기 리스트”

1. `var / let / const` 차이 (스코프, 재선언/재할당, 호이스팅)
2. 원시 타입 vs 참조 타입 (복사 방식, 불변/가변)
3. `==` vs `===`, 논리 연산자의 단축 평가
4. 함수 선언식 vs 표현식 vs 화살표 함수 (호이스팅, this)
5. 기본 매개변수 / 나머지 매개변수 / 전개 구문
6. `for`, `while`, `for...in`, `for...of` 각 목적
7. 객체 속성 참조(dot/bracket), `'key' in obj`
8. JSON.stringify / JSON.parse 흐름
9. Array Helper (`forEach`, `map`, `filter`, `find`, `some`, `every`, `reduce`) 역할
10. 콜백 함수 정의 & 장점(유연성 + 비동기)
11. class/constructor/new 기본 구조
12. DOM 개념, `document` 역할, 주요 선택자(`querySelector`)
13. `textContent` vs `innerHTML` 차이
14. 이벤트 리스너 패턴: 선택 → `addEventListener` → 콜백 안에서 DOM 조작
15. 이벤트 버블링/캡처링, 이벤트 위임, `event.target`/`currentTarget`
16. `preventDefault()` / `stopPropagation()`
17. input / keyup / scroll / drag & drop 주요 이벤트 흐름

'''