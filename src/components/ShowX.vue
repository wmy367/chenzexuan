<template>
    <div class="bg-lv" >
        <div class="ct-lv" >
            <div class="ct-cc">
                <van-icon name="like" color="#F56C6C" size="100" @click="open1" />
            <!-- <van-icon name="like" size="100"/> -->
            </div>
        </div>

    </div>
</template>

<script>
import Vue from 'vue';
import { Icon } from 'vant';
// import { }

Vue.use(Icon);

export default {
    name: 'ShowX',
    data: function(){
        return {
            username: 'wmy367',
            password : '',
            msgDatas: ['爱你','阳哥爱你','一直爱你','阳哥就是爱你', '......','... ??? 点的可以了啊 !!!'],
            mindex: 0
        }
    },
    methods: {
        open1() {
            // this.$message.error('错了哦，这是一条错误消息');
            var _this = this;
            _this = this;
            this.username = this.msgDatas[this.mindex]
            this.$message({
                // message: _this.msgDatas[_this.index],
                message: _this.username,
                center: true,
                // type: 'error',
                iconClass: 'el-icon-star-on',
                customClass: "msg-list",
                onClose: this.close1
            });
            _this.mindex = _this.mindex + 1;
            if(_this.mindex >= 6){
                _this.mindex = 6;
            }
        },
        close1(){
            if(this.mindex>0){
                this.mindex = this.mindex - 1
            }else{
                this.mindex = 0;
            }
        }
    }
}
</script>

<style scoped>
.bg-lv {
    padding: 2em;
    /* color: bisque; */
    /* position:absolute; */
    /* width:50%;  */
    /* height:50%; */
    /* background-color:burlywood; */
    /* border: 1rem solid #E6A23C; */
    border-radius: 2em;
    margin-top: 10em;
    margin: 2rem;
    background-color: black;
}

.ct-lv {
    /* border: 0.06rem solid #409EFF; */
    border: 0.1rem solid #E6A23C;
    border-radius: 2em;
    /* background-color: rgb(52, 102, 114); */
    widows: 100%;
    height: 100%;
    min-height: 10em;
    background-color: black;
    margin-top: 2em;
}

.ct-cc {
    margin-top: 8em;
    margin-bottom: 8em;
}

.msg-list{
    background-color: #F56C6C;
    color: red;
    border: 0.1rem solid #67C23A;
}
</style>

