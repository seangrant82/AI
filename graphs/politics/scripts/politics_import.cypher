CREATE CONSTRAINT ON (p:person) ASSERT p:person IS UNIQUE;

:auto USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM 'file:///politics_prez.csv' AS row 

MERGE (p:person  {name:coalesce(row.name,'UNK')})
MERGE (vp:person {name:row.vice })
MERGE (vp)-[:was_vp_for]->(p)

//sec state
:auto USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM 'file:///politics_state.csv' AS row 

MERGE (p:person  {name:coalesce(row.president,'UNK')})
MERGE (st:person {name:row.name })
MERGE (st)-[:was_sec_state_for]->(p)


//sec def
:auto USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM 'file:///politics_def.csv' AS row 

MERGE (p:person  {name:coalesce(row.president,'UNK')})
MERGE (df:person {name:row.name })
MERGE (df)-[:was_sec_def_for]->(p)

//sec int
:auto USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM 'file:///politics_int.csv' AS row 

MERGE (p:person  {name:coalesce(row.president,'UNK')})
MERGE (in:person {name:row.name })
MERGE (in)-[:was_sec_int_for]->(p)

//sec ag
:auto USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM 'file:///politics_ag.csv' AS row 

MERGE (p:person  {name:coalesce(row.president,'UNK')})
MERGE (ag:person {name:row.name })
MERGE (ag)-[:was_sec_ag_for]->(p)

//atty gen
:auto USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM 'file:///politics_atty_gen.csv' AS row 

MERGE (p:person  {name:coalesce(row.president,'UNK')})
MERGE (atty:person {name:row.name })
MERGE (atty)-[:was_atty_gen_for]->(p)
