from agents.document_segmenter import DocumentSegmenter
from agents.summary_agent import SummaryAgent
from agents.integrator_agent import IntegratorAgent
from agents.quality_assurance_agent import QualityAssuranceAgent
from communication.message_queue import MessageQueue

def main():
    # Initialize the message queue
    message_queue = MessageQueue()

    # Initialize the agents
    document_segmenter = DocumentSegmenter(message_queue)
    summary_agent = SummaryAgent(message_queue)
    integrator_agent = IntegratorAgent(message_queue)
    quality_assurance_agent = QualityAssuranceAgent(message_queue)

    # Read and segment the document
    document_segmenter.segment_document('path_to_your_pdf_file')

    # Generate summaries
    summary_agent.generate_summaries()

    # Refine summaries
    integrator_agent.refine_summaries()

    # Final review and adjustment
    quality_assurance_agent.review_summary()

    # Get the final summary
    final_summary = quality_assurance_agent.get_final_summary()

    print(final_summary)

if __name__ == "__main__":
    main()