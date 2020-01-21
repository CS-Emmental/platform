export function slug(title: string):string {
  return title.toLowerCase().replace(/ /g, '-');
}

export default slug;