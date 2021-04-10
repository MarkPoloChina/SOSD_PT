<template>
  <div class="main">
    <div class="logo">
      <img src="static/logo.png">
    </div>
    <div class="text">
      <h2> 大宝贝助手</h2>
    </div>
    <div class="info">
      <p v-if="files.length==0">选择要上传的文件</p>
      <ul v-if="files.length!=0" class="file_list">
        <li v-for="(file,index) in files" :key='index'>{{file.name}}</li>
      </ul>
    </div>
    <div class="cutting">
      <ImgCutter @cutDown="cutDown">
        <button type="button" class="swt_btn" slot="open">选择文件</button>
      </ImgCutter>
      <br>
      <button type="button" class="upl_btn" @click="submit">上传文件</button>
    </div>
  </div>
</template>

<script>
import ImgCutter from 'vue-img-cutter'
import axios from 'axios'
export default {
  name: 'index',
  data () {
    return {
      files: []
    }
  },
  methods: {
    submit () {
      if (this.files.length === 0) { return }
      var i
      var formdata = new FormData()
      for (i = 0; i < this.files.length; i++) {
        formdata.append('files', this.files[i])
      }
      axios({
        method: 'post',
        url: 'http://localhost:5000/bdu/upload',
        data: formdata,
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      })
    },
    cutDown (event) {
      this.files.push(event.file)
    }
  },
  components: {
    ImgCutter
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .logo
  {
    width: 100%;
    padding-top: 100px;
    padding-bottom: 100px;
    background-color: #313131;
  }
  .text
  {
    padding-top: 20px;
  }
  .swt_btn
  {
    display: inline-block;
    margin-top: 20px;
    margin-bottom: 20px;
    width: 200px;
    height: 70px;
    background: #60a9c1;
    font-size: 120%;
    color: rgb(255, 255, 255);
    border-radius: 10px;
    border: none;
  }
  .swt_btn:focus
  {
    outline: none;
  }
  .swt_btn:hover
  {
    cursor: pointer;
    transform: scale(1.1);
    transition-property: all;
    transition-duration: 0.2s;
    transition-timing-function: linear;
    box-shadow:3px 3px 3px 3px #7e7d7d;
  }
  .upl_btn
  {
    display: inline-block;
    margin-bottom: 20px;
    width: 200px;
    height: 70px;
    background: #5bc189;
    font-size: 120%;
    color: rgb(255, 255, 255);
    border-radius: 10px;
    border: none;
  }
  .upl_btn:focus
  {
    outline: none;
  }
  .upl_btn:hover
  {
    cursor: pointer;
    transform: scale(1.1);
    transition-property: all;
    transition-duration: 0.5s;
    transition-timing-function: linear;
    box-shadow:3px 3px 3px 3px #7e7d7d;
  }
  .file_list
  {
    color: #4baada;
    list-style: none;
    padding-left: 0px;
  }
  p{
    color: #4baada
  }
</style>
