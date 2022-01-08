"""
Module that computes the in-depth statistics
"""


def compute_statistics(quiz_data):
    statistics = dict()

    statistics.update(
        {"question_that_should_be_harder"}, __compute_question_harder(quiz_data)
    )

    statistics.update(
        {"question_that_should_be_easier"}, __compute_question_easier(quiz_data)
    )

    statistics.update(
        {"question_with_most_wrong_answers"}, __compute_question_wrong_answer(quiz_data)
    )

    return statistics


def __compute_question_harder(quiz_data):
    """
    Computes top 5 questions that should be harder
    """
    questions = quiz_data["questions"]

    facility_index_mean = sum(
        [question["facility_index"] for question in questions]
    ) / len(questions)

    questions.sort(key=lambda x: x["facility_index"])

    return {"top_questions": questions[:5], "facility_index_mean": facility_index_mean}


def __compute_question_easier(quiz_data):
    """
    Computes top 5 questions that should be easier
    """
    questions = quiz_data["questions"]

    facility_index_mean = sum(
        [question["facility_index"] for question in questions]
    ) / len(questions)

    questions.sort(key=lambda x: x["facility_index"], reverse=True)

    return {"top_questions": questions[:5], "facility_index_mean": facility_index_mean}


def __compute_question_wrong_answer(quiz_data):
    """
    Computes top 5 questions with the most wrong answers
    """
    questions = quiz_data["questions"]

    questions.sort(
        key=lambda question: max(
            [
                answer["frequency"] if answer["partial_credit"] == 0 else 0
                for answer in question["answers"]
            ]
        ),
        reverse=True,
    )

    return {"top_questions": questions[:5]}
