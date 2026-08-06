// Useful MongoDB dashboard queries
db.security_events.countDocuments({})
db.security_events.countDocuments({severity:"Critical"})
db.security_events.find({risk_score:{$gte:75}}).sort({risk_score:-1}).limit(20)
db.security_events.aggregate([{$group:{_id:"$severity",count:{$sum:1}}}])
db.security_events.aggregate([{$group:{_id:"$mitre_technique",count:{$sum:1}}},{$sort:{count:-1}}])
db.security_events.aggregate([{$group:{_id:"$event_type",count:{$sum:1}}}])
