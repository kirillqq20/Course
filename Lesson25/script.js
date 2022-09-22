db.getCollection("companies").find({name: "Wetpaint",number_of_employees: {"$lte" : 47, "$gte" : 45}})
db.getCollection("companies").find({number_of_employees: {"$lt" : 5}, founded_year: {"$gt" : 2012}})
db.getCollection("companies").find({permalink: "supercool-school", deadpooled_year: 2012})
[{
    $group: {
     _id: '$author',
     authors: {
      $first: '$authors'
     }
    }
   }]