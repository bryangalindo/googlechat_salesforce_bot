UNASSIGNED_RECORDS_QUERY = """
                                SELECT
                                    caseNumber
                                    , Subject
                                    , Description
                                    , Priority
                                    , ownerID
                                    , IsClosed
                                FROM case
                                WHERE
                                    ownerID IN ('00G0d000003WBGaEAO','00G320000037CgyEAE',
                                    '00G32000003GXSKEA4', '00G32000002swrIEAQ') AND
                                    IsClosed = False
                               """

ASSIGNED_RECORDS_QUERY = """
                            SELECT caseNumber
                            FROM case
                            WHERE
                                CaseNumber IN {} AND
                                ownerID NOT IN ('00G0d000003WBGaEAO',
                                                '00G320000037CgyEAE')
                         """

TEST_SINGLE_RECORD_QUERY = """
                            SELECT
                                caseNumber
                                , Subject
                                , Description
                                , Priority
                                , ownerID
                            FROM case
                            WHERE caseNumber='00942882'
                            """

GET_CASE_NUMBERS_QUERY = """
                            SELECT case_number
                            FROM cases
                         """

TEST_MULTI_RECORD_QUERY = """
                    SELECT
                        caseNumber
                        , Subject
                        , Description
                        , Priority
                        , ownerID
                    FROM case
                    WHERE caseNumber in ('00943037', '00942913', '00943808')
                    """

CREATE_TABLE_QUERY = """
                     CREATE TABLE IF NOT EXISTS cases (
                            case_number text,
                            subject text,
                            description text,
                            priority text,
                            owner_id text,
                            is_active int,
                            timestamp text,
                            UNIQUE(case_number)
                    )
                     """

CHECK_EXISTING_CASES_QUERY = """
                                SELECT case_number
                                FROM cases
                                WHERE case_number IN {}
                            """

INSERT_INTO_TABLE_QUERY = "INSERT INTO cases VALUES (?, ?, ?, ?, ?, ?, ?)"
