from data_processor import ProcessorConfig, UserDataProcessor
import json
from pathlib import Path
import logging

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def save_results(results, output_file: str):
    """保存结果到JSON文件"""
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    logger.info(f"结果已保存到: {output_file}")

def main():
    """示例用法"""
    # 1. 创建配置
    config = ProcessorConfig(
        seed=42,
        min_length=50,
        max_length=1000,
        quality_threshold=0.7,
        complexity_threshold=0.5,
        dataset_size=10,
        use_ai_model=True,
        model_temperature=0.4,
        max_tokens=4096
    )
    
    # 2. 创建处理器
    processor = UserDataProcessor(config)
    
    # 3. 准备测试数据 - 使用包含多个相关信息的文本
    test_texts = [
        # 科技发展链式关系
        """
        The invention of transistors revolutionized electronics in the 1950s. 
        These tiny semiconductor devices enabled the development of smaller and more 
        efficient computers. The miniaturization of computers led to the creation of 
        personal computers in the 1980s, which transformed how people work and communicate. 
        This digital revolution eventually gave rise to the internet, connecting billions 
        of people worldwide. Today, this interconnected network powers artificial 
        intelligence systems that are reshaping various industries.
        """,
        
        # 环境变化因果链
        """
        Industrial activities have significantly increased carbon dioxide emissions since 
        the Industrial Revolution. These elevated CO2 levels have enhanced the greenhouse 
        effect, trapping more heat in Earth's atmosphere. The rising global temperatures 
        have accelerated the melting of polar ice caps, which has led to rising sea levels. 
        Coastal communities are now facing increased flooding risks, forcing many to 
        consider relocation. This migration pattern is creating new challenges for urban 
        planning and resource management.
        """,
        
        # 生物进化链
        """
        The discovery of antibiotics began with Alexander Fleming's observation of 
        penicillin in 1928. The widespread use of these medications has saved countless 
        lives from bacterial infections. However, the extensive use of antibiotics has 
        led to the evolution of resistant bacteria strains. These superbugs now pose 
        a significant challenge to modern medicine, requiring the development of new 
        treatment approaches. Scientists are exploring alternative solutions like 
        bacteriophage therapy to combat antibiotic resistance.
        """
    ]
    
    # 4. 处理单个文本
    logger.info("开始处理单个文本示例...")
    single_result = processor.process_text(
        test_texts[0],
        source="technology_evolution"
    )
    
    # 保存单个文本处理结果
    save_results(single_result, "single_text_results.json")
    
    # 5. 批量处理文本
    logger.info("开始批量处理文本...")
    batch_results = processor.process_batch(
        test_texts,
        sources=["tech_evolution", "climate_change", "medical_evolution"]
    )
    
    # 保存批量处理结果
    save_results(batch_results, "batch_results.json")
    
    # 6. 打印示例结果
    print("\n=== 单个文本处理结果示例 ===")
    if single_result:
        for i, result in enumerate(single_result, 1):
            print(f"\n文本 {i}:")
            print(f"来源: {result['metadata']['source']}")
            print(f"复杂度: {result['metadata']['complexity']:.2f}")
            print("\n问答对:")
            for j, qa in enumerate(result['qa_pairs'], 1):
                print(f"\n问答对 {j}:")
                print(f"类型: {qa['type']}")
                print(f"问题: {qa['question']}")
                print("推理步骤:")
                for step_num, step in enumerate(qa.get('reasoning_steps', []), 1):
                    print(f"{step_num}. {step}")
                print(f"答案: {qa['answer']}")
                print("支持事实:")
                for fact_num, fact in enumerate(qa.get('supporting_facts', []), 1):
                    print(f"{fact_num}. {fact}")
    
    print("\n=== 批量处理结果统计 ===")
    print(f"总共处理文本数: {len(test_texts)}")
    print(f"生成问答对总数: {sum(len(result['qa_pairs']) for result in batch_results)}")
    
    # 7. 分析结果
    multi_hop_qa = sum(
        1 for result in batch_results
        for qa in result['qa_pairs']
        if qa['type'] == 'multi_hop_qa'
    )
    template_generated = sum(
        1 for result in batch_results
        for qa in result['qa_pairs']
        if qa['type'] == 'template_generated_multi_hop'
    )
    
    print("\n=== 生成方式统计 ===")
    print(f"AI生成多跳问答对数量: {multi_hop_qa}")
    print(f"模板生成多跳问答对数量: {template_generated}")
    
    # 8. 分析推理步骤
    avg_steps = sum(
        len(qa.get('reasoning_steps', []))
        for result in batch_results
        for qa in result['qa_pairs']
    ) / sum(len(result['qa_pairs']) for result in batch_results)
    
    print(f"\n平均推理步骤数: {avg_steps:.2f}")
    
    # 9. 计算平均复杂度
    avg_complexity = sum(
        result['metadata']['complexity']
        for result in batch_results
    ) / len(batch_results)
    
    print(f"平均复杂度分数: {avg_complexity:.2f}")

if __name__ == "__main__":
    main() 