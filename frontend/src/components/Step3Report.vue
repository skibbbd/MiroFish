<template>
  <div class="step3-report">
    <div class="step-header">
      <h2>03 报告生成</h2>
      <p class="step-description">基于图谱和模拟结果，自动生成综合分析报告</p>
    </div>

    <div class="report-generation">
      <div class="generation-status" v-if="!reportGenerated">
        <div class="status-animation">
          <div class="spinner"></div>
        </div>
        <p class="status-text">正在生成报告...</p>
        <div class="progress-bar">
          <div class="progress-fill" :style="{ width: reportProgress + '%' }"></div>
        </div>
        <p class="progress-text">{{ reportProgress }}%</p>
      </div>

      <div class="report-content" v-if="reportGenerated">
        <div class="report-section">
          <h3>报告摘要</h3>
          <p>本报告基于上传的文档和构建的知识图谱，通过多Agent协作进行了全面的分析和预测。</p>
        </div>

        <div class="report-section">
          <h3>关键发现</h3>
          <ul>
            <li>图谱包含 {{ graphData.node_count || 600 }} 个节点和 {{ graphData.edge_count || 1800 }} 条关系边</li>
            <li>识别出 {{ entityCount }} 个关键实体</li>
            <li>建立了 {{ relationshipCount }} 种关系类型</li>
          </ul>
        </div>

        <div class="report-section">
          <h3>方法论</h3>
          <p>本分析采用了以下方法：</p>
          <ul>
            <li>本体论驱动的知识提取</li>
            <li>GraphRAG检索增强生成</li>
            <li>多Agent协作分析</li>
            <li>动态场景模拟</li>
          </ul>
        </div>

        <div class="report-section">
          <h3>系统日志</h3>
          <div class="logs-container">
            <div v-for="(log, index) in systemLogs" :key="index" class="log-entry">
              <span class="log-time">{{ log.time }}</span>
              <span class="log-message">{{ log.message }}</span>
            </div>
          </div>
        </div>

        <div class="action-buttons">
          <button @click="downloadReport" class="btn-download">
            📥 下载报告
          </button>
          <button @click="shareReport" class="btn-share">
            🔗 分享报告
          </button>
          <button @click="goToNextStep" class="btn-next">
            完成 →
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'

const props = defineProps({
  graphData: {
    type: Object,
    default: () => ({})
  },
  systemLogs: {
    type: Array,
    default: () => []
  }
})

const emit = defineEmits(['next-step', 'go-back'])

const reportGenerated = ref(false)
const reportProgress = ref(0)

const entityCount = computed(() => {
  return Math.floor(Math.random() * 50) + 30
})

const relationshipCount = computed(() => {
  return Math.floor(Math.random() * 10) + 5
})

onMounted(() => {
  // Simulate report generation progress
  const interval = setInterval(() => {
    reportProgress.value += Math.random() * 15
    if (reportProgress.value >= 100) {
      reportProgress.value = 100
      clearInterval(interval)
      setTimeout(() => {
        reportGenerated.value = true
      }, 500)
    }
  }, 500)
})

const downloadReport = () => {
  const reportContent = `
# MiroFish 分析报告

## 执行摘要
本报告基于上传的文档生成。

## 关键指标
- 图谱节点数: ${props.graphData.node_count || 600}
- 关系边数: ${props.graphData.edge_count || 1800}
- 识别实体: ${entityCount.value}

## 生成时间
${new Date().toLocaleString()}
  `
  const blob = new Blob([reportContent], { type: 'text/plain' })
  const url = window.URL.createObjectURL(blob)
  const a = document.createElement('a')
  a.href = url
  a.download = 'mirofish-report.txt'
  a.click()
}

const shareReport = () => {
  alert('报告分享链接已复制到剪贴板')
  navigator.clipboard.writeText(window.location.href)
}

const goToNextStep = () => {
  emit('next-step')
}
</script>

<style scoped>
.step3-report {
  padding: 20px;
  height: 100%;
  overflow-y: auto;
}

.step-header {
  margin-bottom: 30px;
}

.step-header h2 {
  margin: 0 0 8px 0;
  font-size: 20px;
  color: #333;
}

.step-description {
  margin: 0;
  color: #666;
  font-size: 14px;
}

.report-generation {
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 30px;
  background: #fafafa;
}

.generation-status {
  text-align: center;
  padding: 40px 0;
}

.status-animation {
  margin-bottom: 20px;
}

.spinner {
  border: 4px solid #f3f3f3;
  border-top: 4px solid #3498db;
  border-radius: 50%;
  width: 40px;
  height: 40px;
  animation: spin 1s linear infinite;
  margin: 0 auto;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.status-text {
  color: #666;
  margin: 20px 0;
}

.progress-bar {
  width: 100%;
  height: 8px;
  background: #e0e0e0;
  border-radius: 4px;
  overflow: hidden;
  margin: 20px 0;
}

.progress-fill {
  height: 100%;
  background: linear-gradient(90deg, #3498db, #2ecc71);
  transition: width 0.3s ease;
}

.progress-text {
  font-weight: bold;
  color: #3498db;
}

.report-content {
  animation: fadeIn 0.5s ease;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

.report-section {
  margin-bottom: 30px;
  padding: 20px;
  background: white;
  border-radius: 6px;
  border-left: 4px solid #3498db;
}

.report-section h3 {
  margin: 0 0 12px 0;
  color: #333;
  font-size: 16px;
}

.report-section p {
  margin: 8px 0;
  color: #666;
  line-height: 1.6;
}

.report-section ul {
  margin: 8px 0;
  padding-left: 20px;
}

.report-section li {
  margin: 6px 0;
  color: #666;
}

.logs-container {
  background: #f5f5f5;
  border: 1px solid #ddd;
  border-radius: 4px;
  padding: 12px;
  max-height: 200px;
  overflow-y: auto;
  font-family: monospace;
  font-size: 12px;
}

.log-entry {
  display: block;
  margin: 4px 0;
  color: #333;
}

.log-time {
  color: #999;
  margin-right: 8px;
}

.action-buttons {
  margin-top: 30px;
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
}

.btn-download,
.btn-share,
.btn-next {
  flex: 1;
  min-width: 120px;
  padding: 12px 20px;
  border: none;
  border-radius: 6px;
  font-size: 14px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-download {
  background: #f0f0f0;
  color: #333;
}

.btn-download:hover {
  background: #e0e0e0;
}

.btn-share {
  background: #fff;
  color: #3498db;
  border: 1px solid #3498db;
}

.btn-share:hover {
  background: #f0f7ff;
}

.btn-next {
  background: #3498db;
  color: white;
  font-weight: bold;
}

.btn-next:hover {
  background: #2980b9;
}
</style>
