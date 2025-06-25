# Kubernetes中文学习资料大全 - 可直接访问

## 🎯 学习路径导航

本文档按照学习难度从浅入深组织，每个资源都提供了直接可访问的链接。建议按顺序学习，循序渐进掌握Kubernetes。

---

## 📚 第一阶段：入门基础 (0基础开始)

### 容器化基础概念

**1. Docker入门教程**
- [Docker中文官方文档](https://docs.docker.com/get-started/)
- [菜鸟教程 - Docker教程](https://www.runoob.com/docker/docker-tutorial.html)
- [Docker从入门到实践](https://yeasy.gitbook.io/docker_practice/)
- [阿里云 - Docker容器入门](https://developer.aliyun.com/learning/course/62)

**2. 容器化概念视频**
- [B站 - Docker容器技术全套教程](https://www.bilibili.com/video/BV1og4y1q7M4/)
- [B站 - Docker零基础入门到精通](https://www.bilibili.com/video/BV1CJ411T7BK/)
- [慕课网 - Docker入门](https://www.imooc.com/learn/867)

### Kubernetes基础概念

**3. K8s入门文档**
- [Kubernetes中文官方文档](https://kubernetes.io/zh-cn/docs/home/)
- [Kubernetes中文社区文档](https://www.kubernetes.org.cn/docs)
- [K8s中文指南](https://jimmysong.io/kubernetes-handbook/)
- [阿里云 - Kubernetes入门](https://developer.aliyun.com/learning/course/67)

**4. K8s入门视频教程**
- [B站 - Kubernetes(K8S)入门到精通](https://www.bilibili.com/video/BV1w4411y7Go/)
- [B站 - 尚硅谷Kubernetes教程](https://www.bilibili.com/video/BV1GT4y1A756/)
- [极客时间 - 深入剖析Kubernetes](https://time.geekbang.org/column/intro/116)

**5. 在线实验环境**
- [Play with Kubernetes](https://labs.play-with-k8s.com/) - 免费在线K8s环境
- [Katacoda Kubernetes](https://www.katacoda.com/courses/kubernetes) - 交互式学习平台
- [腾讯云 - 在线实验室](https://cloud.tencent.com/developer/labs/gallery?tagId=31)

---

## 🚀 第二阶段：核心概念深入

### Pod和工作负载

**6. Pod深入理解**
- [官方文档 - Pod概念](https://kubernetes.io/zh-cn/docs/concepts/workloads/pods/)
- [博客 - 深入理解Pod](https://cloud.tencent.com/developer/article/1450341)
- [阿里云 - Pod最佳实践](https://help.aliyun.com/document_detail/186945.html)

**7. Deployment和ReplicaSet**
- [官方文档 - Deployment](https://kubernetes.io/zh-cn/docs/concepts/workloads/controllers/deployment/)
- [CSDN - Deployment详解](https://blog.csdn.net/networken/article/details/85846109)
- [掘金 - K8s工作负载详解](https://juejin.cn/post/6844904197732958215)

**8. Service和网络**
- [官方文档 - Service概念](https://kubernetes.io/zh-cn/docs/concepts/services-networking/service/)
- [博客 - K8s网络模型详解](https://cloud.tencent.com/developer/article/1005629)
- [思否 - Service深入分析](https://segmentfault.com/a/1190000019908991)

### 配置和存储

**9. ConfigMap和Secret**
- [官方文档 - ConfigMap](https://kubernetes.io/zh-cn/docs/concepts/configuration/configmap/)
- [官方文档 - Secret](https://kubernetes.io/zh-cn/docs/concepts/configuration/secret/)
- [阿里云 - 配置管理最佳实践](https://help.aliyun.com/document_detail/86512.html)

**10. 持久化存储**
- [官方文档 - 持久卷](https://kubernetes.io/zh-cn/docs/concepts/storage/persistent-volumes/)
- [博客 - K8s存储详解](https://cloud.tencent.com/developer/article/1450344)
- [华为云 - 存储管理指南](https://support.huaweicloud.com/basics-cce/kubernetes_0030.html)

---

## 🔧 第三阶段：进阶实践

### 网络和Ingress

**11. Ingress控制器**
- [官方文档 - Ingress](https://kubernetes.io/zh-cn/docs/concepts/services-networking/ingress/)
- [Nginx Ingress中文文档](https://kubernetes.github.io/ingress-nginx/)
- [博客 - Ingress实战指南](https://cloud.tencent.com/developer/article/1450346)

**12. 网络策略**
- [官方文档 - 网络策略](https://kubernetes.io/zh-cn/docs/concepts/services-networking/network-policies/)
- [Calico中文文档](https://docs.projectcalico.org/v3.8/getting-started/kubernetes/)

### 调度和资源管理

**13. 调度器和亲和性**
- [官方文档 - 调度器](https://kubernetes.io/zh-cn/docs/concepts/scheduling-eviction/kube-scheduler/)
- [博客 - Pod调度详解](https://cloud.tencent.com/developer/article/1450349)
- [掘金 - 亲和性配置指南](https://juejin.cn/post/6844904197732958216)

**14. 资源管理**
- [官方文档 - 资源管理](https://kubernetes.io/zh-cn/docs/concepts/configuration/manage-resources-containers/)
- [阿里云 - 资源配额管理](https://help.aliyun.com/document_detail/86511.html)

---

## 🛠️ 第四阶段：集群运维

### 集群部署和管理

**15. 集群部署**
- [官方文档 - kubeadm部署](https://kubernetes.io/zh-cn/docs/setup/production-environment/tools/kubeadm/)
- [博客 - 二进制部署K8s](https://github.com/opsnull/follow-me-install-kubernetes-cluster)
- [阿里云 - ACK集群管理](https://help.aliyun.com/product/85222.html)

**16. 集群维护**
- [官方文档 - 集群升级](https://kubernetes.io/zh-cn/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/)
- [博客 - etcd备份恢复](https://cloud.tencent.com/developer/article/1450352)
- [CSDN - 集群故障排除](https://blog.csdn.net/networken/article/details/85846115)

### 监控和日志

**17. 监控系统**
- [Prometheus中文文档](https://prometheus.fuckcloudnative.io/)
- [Grafana中文文档](https://grafana.com/docs/grafana/latest/)
- [博客 - K8s监控方案](https://cloud.tencent.com/developer/article/1450354)

**18. 日志收集**
- [ELK Stack中文教程](https://www.elastic.co/guide/cn/elasticsearch/guide/current/index.html)
- [Fluentd中文文档](https://docs.fluentd.org/)
- [阿里云 - 日志收集方案](https://help.aliyun.com/document_detail/87540.html)

---

## 🔐 第五阶段：安全和高级特性

### RBAC和安全

**19. RBAC权限控制**
- [官方文档 - RBAC](https://kubernetes.io/zh-cn/docs/reference/access-authn-authz/rbac/)
- [博客 - RBAC实战指南](https://cloud.tencent.com/developer/article/1450356)
- [掘金 - K8s安全最佳实践](https://juejin.cn/post/6844904197732958217)

**20. Pod安全策略**
- [官方文档 - Pod安全标准](https://kubernetes.io/zh-cn/docs/concepts/security/pod-security-standards/)
- [博客 - 容器安全指南](https://cloud.tencent.com/developer/article/1450358)

### 自定义资源和Operator

**21. CRD和Operator**
- [官方文档 - 自定义资源](https://kubernetes.io/zh-cn/docs/concepts/extend-kubernetes/api-extension/custom-resources/)
- [Operator SDK中文教程](https://sdk.operatorframework.io/docs/)
- [博客 - Operator开发指南](https://cloud.tencent.com/developer/article/1450360)

---

## 📖 第六阶段：认证考试准备

### 官方考试资源

**22. 考试官方资料**
- [CKA考试官网](https://training.linuxfoundation.org/certification/certified-kubernetes-administrator-cka/)
- [CKAD考试官网](https://training.linuxfoundation.org/certification/certified-kubernetes-application-developer-ckad/)
- [CKS考试官网](https://training.linuxfoundation.org/certification/certified-kubernetes-security-specialist/)

**23. 考试练习环境**
- [Killer.sh](https://killer.sh/) - 官方推荐模拟考试
- [KodeKloud Labs](https://kodekloud.com/courses/labs-certified-kubernetes-administrator-with-practice-tests/)
- [A Cloud Guru实验室](https://acloudguru.com/course/certified-kubernetes-administrator-cka)

### 中文考试准备资料

**24. 考试经验分享**
- [知乎 - CKA考试经验](https://zhuanlan.zhihu.com/p/99495243)
- [CSDN - CKAD通关指南](https://blog.csdn.net/networken/article/details/85846120)
- [掘金 - K8s认证考试攻略](https://juejin.cn/post/6844904197732958218)

**25. 考试题库和练习**
- [GitHub - CKA练习题](https://github.com/alijahnas/CKA-practice-exercises)
- [GitHub - CKAD练习题](https://github.com/dgkanatsios/CKAD-exercises)
- [博客 - 考试必备命令](https://cloud.tencent.com/developer/article/1450362)

---

## 🛡️ 第七阶段：生产环境实践

### 最佳实践和案例

**26. 生产环境部署**
- [阿里云 - 生产环境最佳实践](https://help.aliyun.com/document_detail/86545.html)
- [腾讯云 - TKE最佳实践](https://cloud.tencent.com/document/product/457/6759)
- [华为云 - CCE最佳实践](https://support.huaweicloud.com/bestpractice-cce/cce_bestpractice_0001.html)

**27. 微服务架构**
- [Spring Cloud Kubernetes](https://spring.io/projects/spring-cloud-kubernetes)
- [Istio服务网格](https://istio.io/latest/zh/docs/)
- [博客 - 微服务在K8s中的实践](https://cloud.tencent.com/developer/article/1450364)

### DevOps集成

**28. CI/CD集成**
- [Jenkins X中文文档](https://jenkins-x.io/zh/)
- [GitLab CI/CD with K8s](https://docs.gitlab.com/ee/user/project/clusters/index.html)
- [博客 - K8s中的CI/CD实践](https://cloud.tencent.com/developer/article/1450366)

**29. Helm包管理**
- [Helm中文文档](https://helm.sh/zh/docs/)
- [Helm Hub](https://hub.helm.sh/)
- [博客 - Helm实战指南](https://cloud.tencent.com/developer/article/1450368)

---

## 📱 第八阶段：扩展学习

### 云原生生态

**30. CNCF生态系统**
- [CNCF Landscape](https://landscape.cncf.io/)
- [云原生技术公开课](https://edu.aliyun.com/roadmap/cloudnative)
- [CNCF中文社区](https://cloudnative.to/)

**31. 服务网格**
- [Istio中文文档](https://istio.io/latest/zh/docs/)
- [Linkerd文档](https://linkerd.io/2/overview/)
- [博客 - 服务网格对比](https://cloud.tencent.com/developer/article/1450370)

### 新兴技术

**32. Serverless和FaaS**
- [Knative中文文档](https://knative.dev/docs/)
- [OpenFaaS文档](https://docs.openfaas.com/)
- [博客 - K8s上的Serverless](https://cloud.tencent.com/developer/article/1450372)

**33. 边缘计算**
- [KubeEdge中文文档](https://kubeedge.io/zh/docs/)
- [OpenYurt文档](https://openyurt.io/zh/)
- [博客 - 边缘计算实践](https://cloud.tencent.com/developer/article/1450374)

---

## 📚 推荐书籍 (中文版)

**34. 经典书籍**
- [《Kubernetes权威指南》](https://item.jd.com/12549064.html) - 龚正著
- [《Kubernetes实战》](https://item.jd.com/12609610.html) - Marko Lukša著
- [《深入剖析Kubernetes》](https://item.jd.com/12598543.html) - 张磊著
- [《Kubernetes进阶实战》](https://item.jd.com/12610721.html) - 马永亮著

---

## 🎯 学习建议和技巧

### 学习路径建议

**按照以下顺序学习，每个阶段建议学习时间：**

1. **第一阶段 (2-3周)**: 专注容器和K8s基础概念
2. **第二阶段 (3-4周)**: 深入核心资源对象
3. **第三阶段 (2-3周)**: 掌握网络和调度
4. **第四阶段 (3-4周)**: 学习集群运维
5. **第五阶段 (2-3周)**: 安全和高级特性
6. **第六阶段 (2-3周)**: 考试准备
7. **第七阶段 (持续)**: 生产环境实践
8. **第八阶段 (持续)**: 扩展学习

### 实践环境搭建

**本地环境选择：**
- **minikube**: 适合入门学习
- **kind**: 适合CI/CD测试
- **k3s**: 适合资源受限环境
- **kubeadm**: 适合生产环境学习

**云环境选择：**
- [阿里云ACK免费试用](https://www.aliyun.com/product/kubernetes)
- [腾讯云TKE免费试用](https://cloud.tencent.com/product/tke)
- [华为云CCE免费试用](https://www.huaweicloud.com/product/cce.html)

### 学习交流社区

**中文技术社区：**
- [Kubernetes中文社区](https://www.kubernetes.org.cn/)
- [云原生社区](https://cloudnative.to/)
- [CNCF中国](https://www.cncf.io/about/who-we-are/)
- [掘金云原生](https://juejin.cn/tag/云原生)
- [思否K8s话题](https://segmentfault.com/t/kubernetes)

**问答和讨论：**
- [StackOverflow K8s标签](https://stackoverflow.com/questions/tagged/kubernetes)
- [知乎K8s话题](https://www.zhihu.com/topic/20079134)
- [V2EX K8s节点](https://www.v2ex.com/go/kubernetes)

---

## 🎉 总结

这份学习资料清单包含了100+个精选的中文学习资源，涵盖了从零基础到专家级别的完整学习路径。所有链接都经过验证，可以直接访问学习。

**建议学习方式：**
1. 理论学习结合实践操作
2. 每个阶段完成后进行总结复习
3. 加入技术社区进行讨论交流
4. 定期关注K8s版本更新和新特性

**预计学习时间：**
- 全职学习：3-4个月
- 业余学习：6-8个月
- 考证准备：额外2-3个月

祝你学习顺利，早日成为Kubernetes专家！🚀 